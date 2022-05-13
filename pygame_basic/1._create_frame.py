from turtle import Turtle
import pygame

pygame.init()

#화면 크기 설정
screen_width =480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("nado game")

#이벤트 루프가 계속 돌아야지 창이 꺼지지 않음

running= True
while running:
    for event in pygame.event.get(): #키보드의 입력을 계속 검사함.
        if event.type ==pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running=False #종료해라

pygame.quit()