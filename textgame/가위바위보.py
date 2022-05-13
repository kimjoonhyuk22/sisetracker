import random

print('가위 바위 보 게임')
print('가위 바위 보를 하는 게임 입니다.')
print('3판 2선승제 입니다.')
count_p=0
count_c=0

for i in range(10):
    computer = random.choice(['가위', '바위', '보'])
    player = input('가위 바위 보 중 하나를 입력하세요: ')

    print('컴퓨터는 {}를 냈습니다.'.format(computer))
    print('플레이어는 {}를 냈습니다.'.format(player))

    if computer == '가위':
        if player == '가위':
            print('무승부')
        elif player == '바위':
            print('플레이어 승리')   
            count_p+=1
        elif player == '보':
            print('컴퓨터 승리')
            count_c+=1

    elif computer == '바위':
        if player == '가위':
            print('컴퓨터 승리')
            count_c+=1
        elif player == '바위':
            print('무승부')
        elif player == '보':
            print('플레이어 승리')
            count_p+=1

    elif computer == '보':
        if player == '가위':
            print('플레이어 승리')
            count_p+=1
        elif player == '바위':
            print('컴퓨터 승리') 
            count_c+=1
        elif player == '보':
            print('무승부')
    if count_c ==3 or count_p==3:
        break

if count_p:
    print('경기 결과는 플레이어 승리')
else:
    print('경기 결과는 컴퓨터 승리')
