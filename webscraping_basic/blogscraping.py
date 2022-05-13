#
# AskDjango : http://facebook.com/askdjango/
#
# 파이썬 공부 목적으로만 사용하시기 바랍니다.
# 장고 웹개발 질문은 http://facebook.com/groups/askdjango/ 를 통해 풀어가세요. :)
#

import re
import itertools
import time
import requests
from datetime import date
from collections import namedtuple, OrderedDict
from bs4 import BeautifulSoup


Category = namedtuple('Category', ['unique_id', 'name'])
Post = namedtuple('Post', ['unique_id', 'url', 'title', 'categories', 'tags', 'html', 'posted_at'])


class NaverBlog(object):
    POST_LIST_URL_FORMAT = 'http://blog.naver.com/PostList.nhn?blogId={blog_id}&currentPage={page}'

    def __init__(self, blog_id):
        self.blog_id = blog_id
        if 'blog.naver.com/PostList.nhn' in self.blog_id:
            matched = re.search(r'\?blogId=([a-zA-Z0-9_]+)', self.blog_id)
            if matched:
                self.blog_id = matched.group(1)
        elif 'blog.naver.com' in self.blog_id:
            matched = re.search(r'blog.naver.com/([a-zA-Z0-9_]+)', self.blog_id)
            if matched:
                self.blog_id = matched.group(1)

    def get_post_list(self):
        post_dict = OrderedDict()

        for page in itertools.count(start=1):
            url = self.POST_LIST_URL_FORMAT.format(blog_id=self.blog_id, page=page)
            print('getting {}'.format(url))
            try:
                r = requests.get(url)
                r.raise_for_status()
            except requests.HTTPError as e:
                print(e)
                break
            else:
                soup = BeautifulSoup(r.text, 'html.parser')
                post_tag_idx_pattern = re.compile(r'post_(\d+)')

                post_tags = soup.findAll(id=post_tag_idx_pattern)

                if not post_tags:
                    break

                for post_tag in post_tags:
                    post_idx = re.match(post_tag_idx_pattern, post_tag.attrs['id']).group(1)

                    title_tag = post_tag.find(id='title_' + post_idx)
                    category_tag = title_tag.select('.cate')[0]
                    category_tag.extract()

                    title = ' '.join(title_tag.text.split())

                    categories = []
                    for tag in category_tag.findAll('a'):
                        unique_id = re.search('categoryNo=(\d+)', tag.attrs['href']).group(1)
                        name = ' '.join(tag.text.split())
                        categories.append(Category(unique_id, name))

                    year, month, day = map(int, re.findall(r'\d+', post_tag.select('.date')[0].text)[:3])
                    posted_at = date(year, month, day)

                    url = post_tag.select('.url a')[0].attrs['href']
                    unique_id = re.search(r'(\d+)$', url).group(1)

                    html = str(post_tag.select('.post-view')[0])

                    # TODO: naver blog 에서 ajax loading 을 시키기 때문에 로딩이 안 됨 ㅠ_ㅠ
                    tags = []
                    for tag_tag in post_tag.select('.post-tag a.tag'):
                        name = ' '.join(tag_tag.text.split())
                        tags.append(name)

                    post = Post(unique_id=unique_id, url=url, title=title, categories=categories, tags=tags, html=html, posted_at=posted_at)
                    if post.unique_id in post_dict:
                        print('duplicated post. quit.')
                        return None

                    post_dict[post.unique_id] = post
                    yield post

            time.sleep(0.5)


if __name__ == '__main__':
    blog = NaverBlog('doginsight')
    for idx, post in enumerate(blog.get_post_list()):
        print(idx+1, post.title, post.posted_at, post.url)