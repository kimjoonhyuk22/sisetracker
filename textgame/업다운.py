import random

print('업다운 게임')
print('생각한 숫자를 맞추는 게임 입니다.')

number = random.randint(1, 99)
count=0

for _ in range(10): 
    guess = input('생각한 숫자를 맞추세요 (1 ~ 99): ')
    count+=1
    if number == int(guess):
        print('생각한 숫자가 맞습니다.')
        break
    elif number > int(guess):
        print('틀렸습니다. 생각한 숫자는 더 큰 숫자 입니다.')
        print('기회는 {} 남았습니다.'.format(10-count))
    else:
        print('틀렸습니다. 생각한 숫자는 더 작은 숫자 입니다.')
        print('기회는 {} 남았습니다.'.format(10-count))
    count+=1