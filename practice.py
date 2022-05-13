'''print(5)
print(-10)
print(3.14)
print(5+2)
print(3*(3+1))
print('바보')
print('바'*7)
print('바보 형')
print(5>10)
print(True)
print(not True)
print(not(5>10))
#여기까지 자료형 숫자 문자 부울형 자료형
''' 

'''
print("우리집 강아지 연탄이는 ")
print("연탄이는 4살이며 산책을 좋아해요")
print("연탄이는 어른일까요? True")
#연탄이를 이름을 바꿔줄때 3번 바꾸면 되지만 여러개면 힘들다 그래서 연탄이란것을 변수로 저장공간으로 만들어서 준다음에 써주면 위에 변수만 바꿔주면 되지
'''
'''
animal = "강아지"
name = "연탄이"
age = 4  #정수형에서 문자형으로 바꾸주려고 str()으로 묶는다
hobby='산책'
is_adult= age>=3 #조건으로도 변수가 가능함.

print("우리집 "+ animal +"  "+name+"는 ")
print(name+"는 "+str(age)+"살이며 "+hobby+"을 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

#다른사람이 위에 있는 변수만 바꿔주면 쓸수 있음 강아지대신 고양이 4살대신 2살 이렇게 바꾸줄수 있음
#변수는 문자 중간에 들어갈수도 있다.대신 위에 값에서 바뀌겠지 하비위에는 들어가야됨.
#+부분을 ,컴바로도 바꾸줄수 있다. ,로 쓸때는 str없이도 쓸수 있다, 대신,쓰면 빈칸이 하나 들어간다
print("우리집 ", animal ,"  ",name,"는 ")
print(name,"는 ",str(age),"살이며 ",hobby,"을 좋아해요")
print(name,"는 어른일까요? ",str(is_adult))
'''
#드래그한뒤 컨트롤하고 슬러시하면 여러문장 동시에됨 해제는 반대로
# ㅇ
# ㅇ
# ㅇ
# 퀴즈
'''
station = "사당"
print(station+"행 열차가 들어오고 있습니다")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다")
'''
#연산자

# print(2**3)#2^3 2의 3제곱이 됨
# print(5/3) 
# print(5//3)
# print(5%3)

# print(3==3)
# print(3>=2)
# print(3+2==5)

# print(1!=3)
# print(not(1!=3))

# print((3>0)and(3>1))
# print((3>0) & (3<5))

# print((3>0) or (3>4))
# print((3>0) | (3>5))

# print(3>4>6)
# print(3>4>2)


#수식33분

# print(2+3*4)
# print((2+3)*4)

# number = 2+3*4
# print(number)
# number=number+2
# number+=2
# print(number)

# print(abs(-5))#절대값
# print(pow(4,2))#제곱
# print(max(5,13))#최대값 찾기
# print(round(3.14))

# from math import*
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

#from random import*

# print(random()) #0.0~1.0
# print(random()*10) #1~10 
# print(int(random()*10)) #1~10 정수화

# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

#from random import*
# print(randrange(1,46)) #1부터 46전까지 즉 45까지

# print(randint(1,45))

#퀴즈

# off =randint(4,28)

# print("오프라인 스터디 모임 날짜는 매월"+str(off)+"일로 선정되었습니다")


#문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 ="나나"
# sentence3= """
# 나는 소년이고 
# 파이썬은 쉬워요
# """
# print(sentence3)

#슬라이싱, 문자열
# jumin="990120-1234567"

# print("성별:"+jumin[7]) #0부터시작
# print("년 : "+jumin[0:2])#0부터2전까지 0,1번째나옴
# print("월 :"+jumin[2:4])

# print("생년월일:"+jumin[:6])
# print("뒷자리:"+jumin[7:])
# print("뒷자리:"+jumin[-7:])#뒤부터 7개 가져와라

# #문자열 처리함수

# python ='Python is Amazing'
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())#첫문자가 대문자면 투루 아님 펄스
# print(len(python))
# print(python.replace("Python","java"))

# index =python.index("n")
# print(index)
# index =python.index("n", index+1) #엔이 한번나오고 두번째 나온 엔을 찾는것

# print(python.find("n"))
# print(python.find("java"))#값이 없으면 -1나옴 , 인덱스로 하면 없는것 찾으면 에러남

# print(python.count("n"))#엔이 몇번나오나

#문자열 포맷

# print("a"+"b")
# print("a","b")
# print("나는 %d살입니다" %20) #d는 정수를 의미
# print("나는 %s을 좋아합니다" %"파이썬") #s는 문자열
# print("Apple은 %c로 시작해요"% "A") #c는 한글자

# print("나는 %s살입니다" %20)
# print("나는 %s색과 %s색을 좋아해요" %("빨강","파랑")) #뒤에 %를 괄호로 묶어야지 차례대로 들어감

# #방법2 포맷함수사용, 숫자를 쓸때는 숫자 바꿀수도 있음
# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨강"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨강"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨강"))

# #방법3
# print("나는{age}살이며 {color}색을 좋아해요".format(age=20,color="빨강"))

# print("나는{age}살이며 {color}색을 좋아해요".format(color="파랑",age=30))

# #방법4(파이썬3.6이상)
# age = 20
# color="빨강"
# print(f"나는{age}살이며 {color}색을 좋아해요") #외부의 변수를 안에다가 가져가다 쓸수있음 1시9분16초

#탈출문자
#print("백문의 불여일견\n백견이 불여일타")

# #print("저는 "나도코딩"입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")

#문장내에서 \"~~\"는 탈출문자
#print("C:\\Users\\User\\Desktop\\잡\\프로그램")
#주소에 있는  \역슬래쉬 오류 없에려면 역슬러쉬 2개써줌됨\\

#\r 커서를 맨앞으로 이동하는것
#print("Red Apple\rPine")
# red 하고 띄어쓰기까지 4칸에 pine이 들어가 파인애플이나옴
#\b 백스페이스( \b 앞의 한글자삭제)
#print("Redd\bPine")

#\t 탭역할을 하는것 4칸띄기
#print("Red\tApple")

#퀴즈 1:17:00 사이트별로 비밀번호 만들어주는 프로그램작성
#예 http://naver.com 
#규칙 http://지우고 처음만나는.을 만나기 전까지 부분중
#남은글자 앞3글자+글자갯수+글자내 e갯수+!로 구성

#pw="http://naver.com"
#pw1=pw[7:-4]
#print(pw[7:-4])
# print(pw1)
# print(pw1[0:3])
# print(len(pw1))
# print(pw1.count("e"))
#print(pw1[0:3]+len(pw1)+pw1.count("e")+"!")
#print(pw1[0:3]+str(len(pw1))+str(pw1.count("e"))+"!")


# url="http://naver.com"
# my_str=url.replace("http://","")
# my_str=my_str[0:my_str.index(".")]
# #인덱스로 위치 찾는데 점이 나온 위치를 찾음 거기까지 자름)
# #print(my_str)

# password= my_str[0:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비번은 {1}입니다".format(url, password))
#1:22:01까지

#리스트 순서를 가진 객체의 집합
#지하철 칸 별로 10명 20명 30명있을때
# subway1=10
# subway2=20
# subway3=30
# 을 묶어서 사용가능
# subway=[10,20,30]


# subway=["유재석","조세호","박명수"]
# print(subway)
# print(subway.index("조세호"))
# #하하추가
# subway.append("하하")
# print(subway)

# #정형돈을 유재석 조세호사이에 추가
# subway.insert(1,"정형돈")
# print(subway)

# #pop 뒤에서 부터 하나씩 꺼내기

# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# #같은사람 몇명인지 확인

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#num_list=[5,2,4,3,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)
 
 #자료형에 구애받지 않고 사용가능
# mix_list=["조세호",20,True]
# num_list=[5,2,4,3,1]
# print(mix_list)
# num_list.extend(mix_list)
# print(num_list)

#사전
#키와 벨류로 이루어짐, 키는 중복이 안됨

# cabinet={3:"유재석",100:"김태호"}
# print(cabinet[3])
#값을 가져오는법은 대괄호로, .get()으로

# print(cabinet.get(3))
# print(cabinet[5]) #출력이 안나오고 뒤에도 하이도 출력안됨
# print("hi")
# print(cabinet.get(5)) #출력이 none 나옴 뒤에도 출력됨

#논말고 기본값을 쓰고싶다. 그럼
#print(cabinet.get(5,"사용가능"))

#키 확인하는방법
#print(3 in cabinet)
#print(5 in cabinet)

# cabinet={"A-3":"유재석","B-100":"김태호"}
#키값은 스트링 문자열로도 가능함
#print(cabinet["A-3"])

#새손님 추가, 업데이트
# cabinet["C-20"]="조세호"
# cabinet["A-3"]="김종국"

# print(cabinet)

# #삭제 
# del cabinet["A-3"]
# print(cabinet)

# #벨류,키들만 출력

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

#모든값 자우기
# cabinet.clear()
# print(cabinet)

#튜블은 리스트와 다르게 추가는 안되지만 변경이 안되는것에 사용함. 대신 속도가 빠름
# menu=("돈까스","치즈까스")
# print(menu[0])

# #menu.add("생선까스")
# #안됨

# # name = "김종국"
# # age = 20
# # hobby ="코딩"
# # print(name,age,hobby)

# (name,age,hobby)=("김종국",20,"코딩")
# #튜블사용하면 한번에 3개 정의할수 있다.

# print(name)

#집합(set) : 중복이 안되고 순서가 없는것을 정의함

# my_set={1,2,3,3,3}
# print(my_set)
# #1,2,3만 출력됨

# java={"유재석","김태호","양세형"}
# python=set(["유재석","박명수"])
# #세트를 리스트로 만들고 나서 셋으로 감쌀수 있음 근데왜 대괄호로 안하지?

# #교집합 구하기 자바파이썬 모두할수있는방법

# print(java & python)
# print(java.intersection(python))

# #합집합 

# print(java|python)
# print(java.union(python))

# #차집합 :자바는 할줄알지만 파이썬은 못하는사람

# print(java-python)
# print(java.difference(python))

# # 이제 파이썬 교육받아서 파이썬 할술 아는사람이 늘어난경우
# python.add("김태호")
# print(python)

# #java를 잊은경우
# java.remove("김태호")
# print(python)
#1:48:44 자료구조 변경

# menu={"커피","우유","쥬스"} #집합 set으로 설정
# print(menu,type(menu))

# menu=list(menu)
# print(menu,type(menu)) #리스트형으로 바꿈

# menu=tuple(menu)
# print(menu,type(menu)) #튜블형으로 바꿈

# menu=set(menu)
# print(menu,type(menu)) #셋형 집합형으로 바꿈

# #셋,집합{}순서없고 중복없는,리스트[],튜블():못바꿈
# #딕셔너리{키:벨류}

#퀴즈 : 댓글이벤트하는데 20명중 댓글작성자중 추첨통해 1명 치킨 3명 커피 받는데

#활용예제
# from random import*
# lst=[1,2,3,4,5]
# print(lst)
# shuffle(lst) #무작위로 썩어줌
# print(lst)
# print(sample(lst,1))

# from random import*
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst)
# coffee=sample(lst,3)
# print("커피당첨자 : {0}".format(coffee[0:3]))
# # chi=lst.difference(coffee)) #차집합쓸라했는데 안됨 우선 3명뽑고 3명 기존 리스트에서 제외하고 기존리스트에서 1명더 뽑는식으로 하면됨! 
# # print("치킨당첨자 :"+chi))

# users=range(1,21)
# users=list(users)

# shuffle(users)

# winners=sample(users,4)#4명을 한번에 뽑고 나눔

# print("치킨당첨자 : {0}".format(winners[0]))
# print("커피당첨자 : {0}".format(winners[1:]))

#if 분기 조건문

# weather=input("오늘 날씨는 어때요?")#커서가 나오고 입력을 기다리게 됨. 그리고 그것은 스트링 문자형태로 저장된다

# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")


# temp=int(input("기온이 어때요?"))
# if 30<=temp:
#     print("더워")
# elif 10<=temp and temp<30:
#     print("날씨 좋네")
# elif 0<=temp <10:
#     print("외투챙기세요")
# else:
#     print("너무 추워 나가지 마세요")


#for문

# print("대기번호 : 1")
# print("대기번호 : 2") #계속 반복할대 100번 1000번할때

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))


# for waiting_no in range(5): # 순차적으로 적을수 있음 0부터 시작
#     print("대기번호 : {0}".format(waiting_no))

#1부터 시작하고 싶으면(1,6) 1부터 6직전까지 5까지 나옴


# starbuks = ["아이언맨","토르", "아이엠 그루트"]
# for customer in starbuks:
#     print("{0}님 커피가 준비되었습니다.".format(customer))

#while 5번 부를때까지 안오면 커피버리는것

# customer = "토르"
# index=5
# while index >= 1:
#     print("{0}님 커피가 준비 되었습니다. 호출이 {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기 되었습니다")




# customer = "토르"
# index =1
# while Ture: 
#     print("{0}님 커피 나왔어요.호출수{1}".format(customer,index))   
#     index += 1

# customer="토르"
# person = "Unknown"

# while person != customer :
#     print("{0}님 커피 나왔어요".format(customer))
#     person=input("이름이 어떻게 되세요? :")
#     print("이 커피는 {0} 것 입니다. 기다려주세요".format(customer))
# print("{0}님 커피는 여기 있습니다 ".format(customer))

#continue, break 반복문안에서 쓰는것, 출석번호순으로 책읽다가 결석한 2,5번 넘길때 사용해보자
# absent=[2,5]#결석
# no_book=[7]#책은 안가져옴, 책안가져오면 그럼 수업끝내고 교무실로 대려가서 혼냄
# for student in range(1,11):
#     if student in absent:
#         continue #2,5번은 아래 있는 프린트 실행안하고 넘김 그리고 계속 반복하는것
#     elif student in no_book: #스튜던트 안에 노북이 있으면
#         print("수업은 여기까지 {0}번은 따라와".format(student))
#         break #반복문자체를 정지함
#     print("{0}번 책을 읽어봐".format(student))


#한줄로 끝내는 for문 활용
# #출석번호 1,2,3, 앞에 100을 붙여서 101 102 103으로 하기로함
# student=[1,2,3,4,5]
# print(student)
# student =[i+100 for i in student]
# print(student)

# #학생들 이름을 길이로 변환하는것
# student = ["iron man", "thor", "i am groot"]
# student = [len(i) for i in student] #랭스에 아이가 스튜던트 차례대로 하나씩 변경되는것
# print(student)

# #대문자로 바꾸기 
# student = ["iron man", "thor", "i am groot"]
# student = [i.upper() for i in student] #랭스에 아이가 스튜던트 차례대로 하나씩 변경되는것
# print(student)

#퀴즈 카카오 택시에서 50명의 승객과 매칭 기회가 있을때, 총탑승승객수 구하는 프로그램 작성
# 조건1 승객별 운행 소요시간 5~50분 사이 난수
# 조건2 당신의 소요시간 5~15분 사이 승객만 매칭가능

# (출력문 예시)
# [0]1번째 손님(소요시간 : 15분)
# [ ]2번째 손님(소요시간 : 50분)
# ....
# [ ]50번째 손님(소요시간 : 16분)

# 총 탑승 승객 : 2명
# from random import*
# m_count=0
# for customer in range(1,51):
#     c_time=randint(5,50)
#     k_time=randint(5,15)

#     if c_time < k_time:
#         matching="o"
#         m_count+=1
#     else :
#         matching=" "

#     print("[{0}] {1}번째 손님 (소요시간 : {2}) ".format(matching,customer,c_time))
# print("총 탑승가능 승객수은 {0}명 입니다.".format(m_count))
 
# 승객의 소요시간과 택시의 대기 시간을 랜덤으로 하고 비교해서 태울수 있는것 인지 확인 카운팅 했는데 문제 이해 잘 못한듯
# 난수중 5~15사이인것만 하는것이었음 조건이 5~15사이로 하면 됬음
# 위에서 k_match 없에고 그냥 if조건을 5<c_time<15 하면 됬음

# from random import*
# cnt=0
# for i in range(1,51):#승객
#     time=randrange(5,51) #소요시간
#     if 5<= time<=15:
#         print("[o] {0}번째 손님 (소요시간:{1})".format(i,time))
#         cnt+=1
#     else :
#         print("[ ] {0}번째 손님 (소요시간:{1})".format(i,time))

# print("총 탑승 승객수{0}".format(cnt))

#함수
# def open_account():#함수 정의할때는 def 함수명하고 (): 이렇게 해줌
#     print("새로운 계좌가 생성되었습니다")

# open_account()#함수 실행

# def deposit(balance,money): #인수 전달값
#     print("입금되었습니다.잔액은{0}원입니다".format(balance+money))
#     return balance+money #반환값
# #전달값 반환값이 다 있는경우

# def withdraw(balance, money):
#     if balance>=money:
#         print("출금이 완료되었습니다. 잔액은{0}원입니다".format(balance-money))
#         return balance-money
#     else: 
#         print("잔액이 부족합니다")
#     return balance

# def withdraw_night(balance,money):#저녁 수수료
#     commission = 100
#     return commission, balance-money-commission #리턴에 2개 반환하기

# balance = 0 
# balance = deposit(balance,1000)
# print(balance)

# balance = withdraw(balance,500)
# print(balance)

# balance = withdraw(balance,2000)
# print(balance)

# commission, balance =withdraw_night(balance,500) #리턴을 2개 받게 되면 리스트 형태로 받게 된다.
# print("수수료는{0}원이며, 잔액은{1}원입니다.".format(commission,balance))

# 기본값 함수에서 기본값 정하기

# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}" \
#         .format(name,age,main_lang))
# #\뒤에 역슬레쉬하면 아래칸과 연결
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# #같은 나이 같은 수업일때 ,나이와 수업을 기본값으로 해준다

# def profile(name, age=17, main_lang="파이썬"): #나이 언어 입력받으면 입력받은것로 입력 안받으면 기본값으로
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}" \
#         .format(name,age,main_lang))
# #\뒤에 역슬레쉬하면 아래칸과 연결
# profile("유재석")
# profile("김태호",25)
#profile("정형돈",,"자바") 중간을 숫자를 비우는건 어케하는거지?

#키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile("유재석",20,"파이썬")
# profile(main_lang="자바",name="김태호",age=20) #결과값이 순서대로 나옴, 키워드로 순서상관없이 호출해줄수 있음

#가변인자를 통한 함수호출

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0} \t 나이: {1}\t".format(name,age),end=" ") #end=" "는 빈칸으로 하면 문장을 출력하고 한줄띄지 말고 바로 출력됨
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석",20,"파이썬","자바","c","C3","c++")
# profile("김태호",25, "파이썬", "포틀린","","","") #뒤에 3개는"" 안해줌 오류남
#이런 상황에서 유재석이 하나더 배우거나 ""없이 써줄때 씀


# def profile(name,age,*language):
#     print("이름 : {0} \t 나이: {1}\t".format(name,age),end=" ") #end=" "는 빈칸으로 하면 문장을 출력하고 한줄띄지 말고 바로 출력됨
#     for lang in language: #lang이라는 그냥 변수 하나 만들어서
#         print(lang,end=" ")#줄바꿈 안하려고 end=" "
#     print()#줄바꿈을 위해서 프린트 써줌 

# profile("유재석",20,"파이썬","자바","c","C3","c++","자바스크립트")
# profile("김태호",25, "파이썬", "포틀린") #뒤에 "" 안해도됨

#지역변수 전역변수
# gun=10 #총
# def checkpoint(soldiers):#경계근무
#     gun = gun -soldiers #2번째 gun은 함수안에서는 gun이 설정이 안되있어서 에러가 난것이다
#     print("[함수내]남은총: {0}".format(gun))

# print("전체총 : {0}".format(gun))
# checkpoint(2)#2명이 경계근무가서 2개가져감
# print("남은총 : {0}".format(gun))

# gun=10 #총, 전역변수
# def checkpoint(soldiers):#경계근무
#     gun= 20 #지역변수
#     gun = gun -soldiers #2번째 gun은 함수안에서는 gun이 설정이 안되있어서 에러가 난것이다. 그래서 바로위에 설정해줌 근대 첫번째 건은 에러 안나넌데?!
#     print("[함수내]남은총: {0}".format(gun))

# print("전체총 : {0}".format(gun))
# checkpoint(2)#2명이 경계근무가서 2개가져감
# print("남은총 : {0}".format(gun))

#그럼 함수안에서는 건은 20인 지역변수이고 그안에 쓰이고 밖에 나감 사라짐 
#그래서 global이란 것으로 전역변수 만들어줘야됨

# gun=10 #총, 전역변수는 함수안에서는 못쓰임.
# def checkpoint(soldiers):#경계근무
#     global gun #전역공간에 있는 건을 사용할거다란것!
#     gun = gun -soldiers #2번째 gun은 함수안에서는 gun이 설정이 안되있어서 에러가 난것이다. 그래서 바로위에 설정해줌 근대 첫번째 건은 에러 안나넌데?!
#     print("[함수내]남은총: {0}".format(gun))

# print("전체총 : {0}".format(gun))
# checkpoint(2)#2명이 경계근무가서 2개가져감
# print("남은총 : {0}".format(gun))
#일반적으로 전역많이 쓰면 헷깔리게 되서 반환값으로 받아서 쓰는게 많다.

# gun=10 #총, 전역변수는 함수안에서는 못쓰임
# def checkpoint_ret(gun,soldier): #리턴으로 받는법, 밖에 있는 건을 가져옴.
#     gun=gun-soldier 
#     print("[함수내]남은총: {0}".format(gun))
#     return gun #바뀐 건을 밖으로 반환함.

# print("전체총 : {0}".format(gun))
# gun=checkpoint_ret(gun,2) #밖에 있던 건이 반환값으로 여기서 바뀌게됨.
# print("남은총 : {0}".format(gun))

#함수 퀴즈
# #표준 체중을 구하는 프로그램을 만들어라 
# 표준체중 = 남자 : 키*키*22, 여자 : 키*키*21 (키단위는 m)
# 조건1 표준체중은 별도의 함수내에서 계산, 함수명 std_weight,
# 전달값 키height,성별gender
# 조건2 표준 체중은 소숫점 둘째 자리까지 표시
# 출력예시 : 키 175cm 남자의 표준체중은 67.38kg 입니다

# def std_weight(height,gender):
#     if gender == "남자" :
#         weight=height*height*0.0001*22
#         weight=round(weight,2)
#     else:
#         weight=height*height*0.0001*21
#         weight=round(weight,2)
#     print("키{0}{1}의 표준체중은 {2}입니다".format(height,gender,weight))

# print("키와 성별(남자,여자)을 입력하면 적정 몸무게를 알려드립니다")
# height=int(input("키는?(단위cm)"))
# gender=input("성별은?(남자,여자로 입력)") #정수형으로 입력받고 싶으면 int로 묶어줘라
# std_weight(height,gender)

# def std_weight(height,gender):
#     if gender == "남자" :
#        return height*height*0.0001*22
#     else:
#        return height*height*0.0001*21

# height= 175
# gender="남자"    
# weight=round(std_weight(height,gender),2)
# print("키{0}{1}의 표준체중은 {2}입니다".format(height,gender,weight))

#파일 입출력

#print("파이썬","자바",sep=",", end="?")#sep는 띄어쓰기가 될지 컴마가 될지 결정해줌 , end는 마지막에쓰이는것
#print("무엇이 더 재밋을까요?")
# import sys
# # print("파이썬","자바",file=sys.stdout)#표준출력으로 출력됨 
# # print("파이썬","자바",file=sys.stderr)#에러로 출력되는것 에러처리를 해줄수 잇음 먼내용지?!

# scores ={"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():#아이템하면 예전에 했던것 처럼 다 나옴
#     print(subject.ljust(8), str(score).rjust(4), sep=" : ") #8개만큼 엘 라이트 왼쪽 정렬해라 

#은행 대기 순번표 001,002,003
# for num in range(1,21):
#     print("대기번호 : "+ str(num).zfill(3)) #zfill은 0으로 채우는것 

# # 표준입력
# answer=input("아무값이나 입력하세요 : ") #문자열형태로 들어간다 숫자 집어 넣으면서 숫자로 쓰고 싶으면 숫자int()로 바꿔줘야됨
# print("입력하는 값은 "+answer+"입니다") #숫자를 집어넣어도 잘나옴 애초에 str 저장되니 안감싸줘도 됨. 

#다양한 출력 포맷
#빈자리는 빈공간으로 두고 오른쪽 정렬해서 10자리 공간 확보
#print("{0:>10}".format(500)) # 10자리공간 확보해서 오른쪽에서 7자리 비어두고 3자리 500입력
#양수일때는 +표시 음수일때 -표시
#print("{0:>+10}".format(500))
#print("{0:>+10}".format(-500))

# 10자리 확보하고 왼쪽정렬하고 빈칸을 밑줄로 채우기
#print("{0:_<10}".format(500))

#3자리마다 콤마찍어주기
#print("{0:,}".format(1000000000000))
#print("{0:+,}".format(1000000000000)) #플러스 붙이게

#3자리마다 콤마찍고 부호 붙이고 자릿수도 확보
#빈자리는 ^로 채우기
#print("{0:^<+30,}".format(1000000000000))
# #소숫점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3)) #2자리까지만 3자리에서 반올림

#파일 입출력

# score_file = open("score.txt","w",encoding="utf8")#오픈을 통해서 열고 파일이름 쓰기목적 인코딩정보에다가 utf8을 정해서 한글을 받아올수 있다. 
# print("수학점수 : 50 ", file = score_file)
# print("영어점수 : 100 ", file = score_file)
# score_file.close() #쓰기 목적으로 파일을 열고 닫는것 자동으로 옆에창(폴더안에) 텍스파일로 저장됨, 만들어진다.

# score_file = open("score.txt","a",encoding="utf8") #a는 업핸드로 뒤에 쓰기, w로 쓰면 덮어쓰기가됨 기존내용지워짐
# score_file.write("과학 : 80 ")
# score_file.write("\n코딩 : 100") #줄바꿈해주려고
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8") #한번에 파일 다 읽기
# print(score_file.read())
# score_file.close()

#한줄한줄 읽어오기
# score_file = open("score.txt","r",encoding="utf8") #한번에 파일 다 읽기
# print(score_file.readline()) #한줄 읽고 커서는 다음줄로이동
# print(score_file.readline())
# print(score_file.readline(),end="") #줄바꿈 안하고 싶을때
# print(score_file.readline())
# score_file.close()

#몇줄인지 모를때 반복문을 통해서 함.
# score_file = open("score.txt","r",encoding="utf8") #한번에 파일 다 읽기
# while True:
#     line = score_file.readline() #라인에 한줄씩 저장하고 라인에 아무것도 저장안되면 나옴.한줄띄어쓴것도 나옴
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# lines=score_file.readlines() #모든 라인은 리스트 형태로 저장함
# for line in lines:
#     print(line, end="")  #한줄 씩 출력함
# score_file.close()


#피클 : 프로그램상에서 만든데이터를 파일로 만드는것, 그럼 다른사람이 받아서 또 쓸수 있는것
#import pickle
# profile_file=open("profile.pickle","wb") #피클에서는 바이너리 (1,0,1,0으로)타입으로 설정해주고 인코딩 설정은 필요없다 
# profile={"이름":"박명수", "나이":"30","취미":["축구","골프","코딩"]  }
# print(profile)
# pickle.dump(profile,profile_file) #프로필에 있는 정보는 파일에 저장함.
# profile_file.close()

# profile_file=open("profile.pickle","rb") #피클에서는 바이너리 (1,0,1,0으로)타입으로 설정해주고 인코딩 설정은 필요없다 
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#with 파일을 열고 쓰고닫는 작업을 했는데 좀더 쉽게 가능함.
# import pickle
# with open("profile.pickle","rb") as profile_file: #프로필 파일에서 읽은파일 프로필파일 변수에 저장
#     print(pickle.load(profile_file))
#클로스 없이 위드문을 쓰고 바로 탈출함
# with open("study.txt","w",encoding="utf8") as study_file: #스터디 문서에 스터디파일을 저장해라
#     study_file.write("파이썬을 공부하고 있어요") #스터디 파일 내용은 ~~이다
#스터디파일에 공부하고 있어요 저장됨
# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read()) #간단히 2문장으로 사용가능


# #퀴즈
# 당신의 회사에서 주1회 작성해야하는 보고서가 있다
# 보고서는 하상 아래와 같은 형태로 출력해야한다
# -x주차 주간보고서-
# 부서 : 
# 이름 :
# 업무요약 : 

# 1주차부터 50주차 까지 보고서파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 1주차.txt로 만든다

# for juca in range(1,11):
#     with open("{0}주차.txt".format(juca),"w",encoding="utf8") as study_file: #스터디 문서에 스터디파일을 저장해라
#         study_file.write("{0}주차 주간보고서\n 부서: \n 이름: \n 업무요약: \n".format(juca))
# #10주차만 만들어짐 파일명이 안바뀌네 , .format(juca)을 바로 뒤에 붙여야했음!!

# juca=1
# juca_file = open("{0}주차.txt".format(juca),"w",encoding="utf8")#오픈을 통해서 열고 파일이름 쓰기목적 인코딩정보에다가 utf8을 정해서 한글을 받아올수 있다. 
# print("수학점수 : 50 ", file = juca_file)
# print("영어점수 : 100 ", file = juca_file)
# juca_file.close() #쓰기 목적으로 파일을 열고 닫는것 자동으로 옆에창(폴더안에) 텍스파일로 저장됨, 만들어진다.


#정답
# for i in range(1,11):
#     with open(str(i)+"주차.txt","w",encoding="utf8") as report_file: #i를쓸때 그냥쓰면 숫자로 되서 안되니까 같은 문자열배열로 만들어주려고 str붙였고 그냥난 포맷썼는데 됬음
#         report_file.write("-{0} 주차 주간보고-".format(i)) 
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무요약 : ")


#클래스, 스타크래프트를 예를 들어서 설명
#마린 : 공격유닛 군인 총을 쏨
# name="마린"
# hp=40
# damage=5

# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력은{0},공격력은 {1}\n".format(hp,damage))

# #탱크 만들기
# tank_name="탱크"
# tank_hp=150
# tank_damage=35

# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력은{0},공격력은 {1}\n".format(tank_hp,tank_damage))


# def attack(name,location,damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 :{2}]".format(name,location,damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# #만약 여기서 탱크가 하나더 추가되면?
# tank2_name="탱크"
# tank2_hp=150
# tank2_damage=35

# print("{0}유닛이 생성되었습니다.".format(tank2_name))
# print("체력은{0},공격력은 {1}\n".format(tank2_hp,tank2_damage))
#이렇게하면 수십수백하는게 매번하는게 힘듬 그래서 클래스가 필요함 
#붕어빵 틀하고 비교하는데 그 틀에 재료를 넣으면 붕어빵 만들어지고 틀은 하나이고 
# 붕어빵은 무한정 만들수 있음 서로 연관이있는 함수와 변수의 집합

#지금까지한것 클래스로 변환

# class Unit:
#     def __init__(self, name, hp, damage): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp,self.damage))

# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)
# tank=Unit("탱크",150,35)

# #__init__ 생성자이다 클래스로 만들어지는 것을 객체라고 하는데 이때 마린과 탱크는 유닛클래스의 인스턴스라고 한다, 객체가 생성될때는 이닛함수에 적힌 셀프배고 나머지 인자를 넣어줘야된다.
# #즉, 이름체력데이지3개 넣어서 만들어줘야됨
# #맴버 변수 self.name 같은 것을 클래스안에서 정의됨 변수

# #레이스 만들기, 클로킹 기능이 있음.
# wraith1=Unit("레이스",80,5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# #마인드 컨트롤 상대방 유닛을 내것으로 뺏음 기능이 있음
# wraith2 =Unit("빼앗은 레이스",80,5)
# wraith2.clocking=True

# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
#클로킹 변수는데 외부에서 추가한것 파이썬에서는 객체에 변수를 추가해서 쓸수 있음
#레이스1에는 클로킹은 없음.

#매소드(클래스내 함수 만들기)
#일반유닛
# class Unit:
#     def __init__(self, name, hp, damage): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp,self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))

# #파이어뱃 공격유닛 화염방사기
# firebat1=AttackUnit("파이어뱃",50,10)
# firebat1.attack("5시")

# #공격받는것 2번
# firebat1.damaged(25)
# firebat1.damaged(25)

#상속 : 유닛에 있는 클래스에 있는 변수를 상속받아서 다른 어택유닛클래스에서 쓸수 있는것 
#상속받고 싶은 클래스 정의함

#매딕 만들기 공격력없음. 
#일반유닛 : 유닛의 name,hp는 어택유닛에서도 있음 그냥 2번안쓰고 상속하면됨
# class Unit:
#     def __init__(self, name, hp): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         print("{0} 유닛이 생성되었습니다".format(self.name))
       

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage): #__init__ 기본설정
#         Unit.__init__(self,name,hp) #상속받은 코드 
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))

# firebat1=AttackUnit("파이어뱃",50,10)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(30)

#다중상속
#상속을 부모클래스를 2개받는것
#일반유닛 : 유닛의 name,hp는 어택유닛에서도 있음 그냥 2번안쓰고 상속하면됨
#공중유닛 같은경우에 공격공중유닛과 드랍쉽같은 공격 안하는 유닛 있음.

# class Unit:
#     def __init__(self, name, hp): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
   
       
# class AttackUnit(Unit): #유닛에서 상속받을거라 괄호안에 유닛넣음
#     def __init__(self, name, hp, damage): #__init__ 기본설정
#         Unit.__init__(self,name,hp) #상속받은 코드를 넣는법
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))

# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self,name,location):
#         print("{0}:{1} 방향을 날아갑니다[속도:{2}]".format(name,location,self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):#2곳 어택유닛과 플라이 에이블에서 상속받음
#     def __init__ (self, name, hp, damage, fly_speed): #클랫스만들때 이닛항상 넣어야됨!! 이것때문에 애먹음
#         AttackUnit.__init__(self,name,hp,damage) #상속받은것1
#         Flyable.__init__(self,fly_speed) #상속받은것2

#발키리 :  공중공격 한번에 14발 미사일 발사

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) #이름 체력 공격력 공중이동속도
# valkyrie.fly(valkyrie.name,"3시") #def fly(self,name,location): 이래서 그런가 name을받을때 그냥 valkyrie 말고 valkyrie.name로 해야됨(발키리에 있는 이름을 가져오는것이니까)


#연산자 오버라이딩, 부모클래스에서 가져오는게 아니고 자식클래스에서 가져오는것

# class Unit: #스피드 추가
#     def __init__(self, name, hp, speed): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.speed = speed

#     def move(self, locatoin):
#         print("[지상유닛이동]")
#         print("{0}:{1}방향으로 이동합니다 [속도{2}]".format(self.name,locatoin,self.speed))



       
# class AttackUnit(Unit): #유닛에서 상속받을거라 괄호안에 유닛넣음
#     def __init__(self, name, hp, speed, damage): #__init__ 기본설정, 스피드 추가
#         Unit.__init__(self,name,hp, speed) #상속받은 코드를 넣는법
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))

# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self,name,location):
#         print("{0}:{1} 방향을 날아갑니다[속도:{2}]".format(name,location,self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):#2곳 어택유닛과 플라이 에이블에서 상속받음
#     def __init__ (self, name, hp, damage, fly_speed): #클랫스만들때 이닛항상 넣어야됨!! 이것때문에 애먹음
#         AttackUnit.__init__(self,name,hp,0,damage) #상속받은것1, 지상스피드는0
#         Flyable.__init__(self,fly_speed) #상속받은것2

#     def move(self, location): #새로운 정의 다른 무브임.
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location) #즉 같은 무브 함수로 다른 클래스의 함수 플라이 불러온것,이름까지여기서 처리함.

# #지상유닛에다가 스피드 추가할것
# #벌처생성,배틀생성
# vulture=AttackUnit("벌처",80,10,20)
# battlecruise=FlyableAttackUnit("배틀크루져",500,25,3)

# vulture.move("11시")
# #battlecruise.fly(battlecruise.name,"9시")
# battlecruise.move("9시") #무브를 쓰고 방향만해도 위에서 이름다 호출했으니 무방함

#메소트 오버로딩만 써서 똑같이 무브만 쓰면 지상 공중둘다 이동하게 함

#PASS

# class Unit: #스피드 추가
#     def __init__(self, name, hp, speed): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.speed = speed

#     def move(self, locatoin):
#         print("[지상유닛이동]")
#         print("{0}:{1}방향으로 이동합니다 [속도{2}]".format(self.name,locatoin,self.speed))



       
# class AttackUnit(Unit): #유닛에서 상속받을거라 괄호안에 유닛넣음
#     def __init__(self, name, hp, speed, damage): #__init__ 기본설정, 스피드 추가
#         Unit.__init__(self,name,hp, speed) #상속받은 코드를 넣는법
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))

# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self,name,location):
#         print("{0}:{1} 방향을 날아갑니다[속도:{2}]".format(name,location,self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):#2곳 어택유닛과 플라이 에이블에서 상속받음
#     def __init__ (self, name, hp, damage, fly_speed): #클랫스만들때 이닛항상 넣어야됨!! 이것때문에 애먹음
#         AttackUnit.__init__(self,name,hp,0,damage) #상속받은것1, 지상스피드는0
#         Flyable.__init__(self,fly_speed) #상속받은것2

#     def move(self, location): #새로운 정의 다른 무브임.
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location) #즉 같은 무브 함수로 다른 클래스의 함수 플라이 불러온것,이름까지여기서 처리함.

# #건물 생성
# class BuildingUnit(Unit): #유닛 상속한것
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name,hp,0) #슈퍼를 쓸때는 유닛대신쓸수 있는데 셀프뺀다.유닛클래스 상속할때 초기화할때 사용가능 대신 다중 상속할대 문제 앞에 상속한것만됨
#         self.location = location


# #서플 생성
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass #그냥 완성된것처럼 만드는것 아직 안했어도

# game_start()
# game_over()

#super
# 상속받을때 쉽게하는것
#스타 전반전
# import random

# class Unit: #스피드 추가
#     def __init__(self, name, hp, speed): #__init__ 기본설정
#         self.name=name
#         self.hp=hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name)) #파라미터로 받은 네임과 그냥 네임 둘다 써도됨 

#     def move(self, locatoin):
#         print("[지상유닛이동]")
#         print("{0}:{1}방향으로 이동합니다 [속도{2}]".format(self.name,locatoin,self.speed))

#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1}입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0}:파괴되었습니다".format(self.name))


       
# class AttackUnit(Unit): #유닛에서 상속받을거라 괄호안에 유닛넣음
#     def __init__(self, name, hp, speed, damage): #__init__ 기본설정, 스피드 추가
#         Unit.__init__(self,name,hp, speed) #상속받은 코드를 넣는법
#         self.damage=damage

#     def attack(self, location): 
#         print("{0}:{1} 방향으로 적군이 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#         #로케이션은 위에 클래스 변수로 정의 되지 않았고 그냥 어택함수에서 로케이션을 받아 쓴다

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,"마린",40,1,5)
# #스팀팩추가 : 공격속도 추가 체력10감소
#     def stimpack(self):
#         if self.hp>10:
#             self.hp -=10
#             print("{0}:스팀팩을 사용합니다(hp 10 감소])".format(self.name))
#         else:
#             print("[0]:체력이 부족하여 스팀팩을 사용하지 못합니다".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부 (클래스 변수)

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
#         self.siege_mode = False # 시즈모드 (해제 상태)
    
#     # 시즈모드
#     def set_siege_mode(self):
#         if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return

#         # 현재 시즈모드가 아닐 때
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2 # 공격력 2배로 증가
#             self.siege_mode = True # 시즈 모드 설정
#         # 현재 시즈모드일 때
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2 # 공격력 절반으로 감소
#             self.siege_mode = False # 시즈 모드 해제


# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)

#     # 클로킹 모드
#     def cloaking(self):
#         # 현재 클로킹 모드일 때
#         if self.cloaked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.cloaked = False
#         # 현재 클로킹 모드가 아닐 때
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.cloaked = True
# # class Flyable:
# #     def __init__(self,flying_speed):
# #         self.flying_speed = flying_speed

# #     def fly(self,name,location):
# #         print("{0}:{1} 방향을 날아갑니다[속도:{2}]".format(name,location,self.flying_speed))

# # class FlyableAttackUnit(AttackUnit,Flyable):#2곳 어택유닛과 플라이 에이블에서 상속받음
# #     def __init__ (self, name, hp, damage, fly_speed): #클랫스만들때 이닛항상 넣어야됨!! 이것때문에 애먹음
# #         AttackUnit.__init__(self,name,hp,0,damage) #상속받은것1, 지상스피드는0
# #         Flyable.__init__(self,fly_speed) #상속받은것2

# #     def move(self, location): #새로운 정의 다른 무브임.
# #         print("[공중 유닛 이동]")
# #         self.fly(self.name,location) #즉 같은 무브 함수로 다른 클래스의 함수 플라이 불러온것,이름까지여기서 처리함.

# def game_start():
#     print("알림 : 새로운 게임을 시작합니다")

# def game_over():
#     print("player :gg ")
#     print("[player님이 퇴장하셨습니다.]")

# game_start
# m1=Marine()
# m2=Marine()
# m3=Marine()
# t1=Tank()
# t2=Tank()
# w1=Wraith()

# attack_units=[]
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)

# #유닛 생성
# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed =True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
#         unit.stimpack()
#     elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
#         unit.cloaking()
#         # 전군 공격

# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# # 게임 종료
# game_over()

# from random import *

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력

#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부 (클래스 변수)

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
#         self.siege_mode = False # 시즈모드 (해제 상태)
    
#     # 시즈모드
#     def set_siege_mode(self):
#         if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return

#         # 현재 시즈모드가 아닐 때
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2 # 공격력 2배로 증가
#             self.siege_mode = True # 시즈 모드 설정
#         # 현재 시즈모드일 때
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2 # 공격력 절반으로 감소
#             self.siege_mode = False # 시즈 모드 해제

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)

#     # 클로킹 모드
#     def cloaking(self):
#         # 현재 클로킹 모드일 때
#         if self.cloaked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.cloaked = False
#         # 현재 클로킹 모드가 아닐 때
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.cloaked = True

# # 게임 시작
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# # 게임 종료
# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
#         unit.stimpack()
#     elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
#         unit.cloaking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# # 게임 종료
# game_over()

# ############################
# #퀴즈 주어진 코드를 통해 부동산 프로그램 작성해라
# 출력예제 총 3개 매물있습니다
# 강남 아파트 매매 10억 2010년
# 마포 오피스 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass

#     # 매물 정보 표시
#     def show_detail(self):
#         pass

#예외처리  try except

#의도적으로 에러만들기(기존에 에러함수가 있는경우)  raise

#사용자 정의 예외처리 clsss로만듬

#파이널리 예외처리중에서 정상이던 예외던 무조건 처리되는것

#퀴즈

#모듈 = 파일 , 다른 파일에 함수 가져다 쓰는것

#패키지(라이브러리) 모듈(파일)을 모은것(하나폴더에 모듈(파일) 모은것)

#__all__




