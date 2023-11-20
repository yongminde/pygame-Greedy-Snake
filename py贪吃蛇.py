#雍明德制作
import pygame
import random
from pygame import locals

print("按Q键或按关闭键退出")
print("上下左右控制或wasd控制")
print("获得十五分结束")
#初始化pygame
pygame.init()
#创建创口
screen=pygame.display.set_mode((660,480))
background=pygame.image.load('bg.png')
right=pygame.image.load('right.png')
body=pygame.image.load('body.png')
pg=pygame.image.load('apple.png')
left=pygame.image.load('left.png')
down=pygame.image.load('down.png')
up=pygame.image.load('up.png')
my_font=pygame.font.Font('neuropol.ttf',18)

x=120
y=150
setheading="right"
tou=right
lista=[(60,120),(60,150),(90,150),(x,y)]
pg_x=360
pg_y=300
dj=0
poi=0
yuih=0

while True:
    for event in pygame.event.get():
        if event.type==locals.QUIT:
            exit()
        if event.type==locals.KEYDOWN:
            if event.key==locals.K_RIGHT and setheading!="left":
                setheading="right"
                tou=right
            if event.key==pygame.K_d:
                setheading="right"
                tou=right
            if event.key==locals.K_LEFT and setheading!="right":
                setheading="left"
                tou=left
            if event.key==pygame.K_a:
                setheading="left"
                tou=left
            if event.key==locals.K_DOWN and setheading!="up":
                setheading="down"
                tou=down
            if event.key==pygame.K_w:
                setheading="up"
                tou=up
            if event.key==locals.K_UP and setheading!="down":
                setheading="up"
                tou=up
            if event.key==pygame.K_s:
                setheading="down"
                tou=down
            #发送彩蛋信息
            if event.key==pygame.K_p:
                dj=20
                poi=1
            if event.key==pygame.K_q:
            #接收到退出事件后退出程序，按Q
                pygame.mouse.set_visible(True)
                exit()
    if setheading=="right":
        x+=30
    elif setheading=="left":
        x-=30
    elif setheading=="down":
        y+=30
    else:
        y-=30
    lista.append((x,y))
    #判断胜利
    if x==pg_x and y==pg_y:
        num1=random.randint(1,22)
        num2=random.randint(1,16)
        pg_x=30*num1-30
        pg_y=30*num2-30
        dj+=1
    else:
        lista.pop(0)
    if x<0 or x>630 or y<0 or y>450:
        yuih=1
        break
    screen.blit(background,(0,0))
    screen.blit(tou,(lista[-1]))
    for i in range(len(lista)-1):
        screen.blit(body,lista[i])
    screen.blit(pg,(pg_x,pg_y))
    info="Score:"+str(dj)
    texe=my_font.render(info,True,(0,0,0))
    screen.blit(texe,(0,0))
    #触发彩蛋
    if poi==1:
        break
    #判断胜利
    if dj>=15:
        break
    pygame.display.update()
    #游戏画面每秒不超过三帧
    FPSCLOCK= pygame.time.Clock();FPSCLOCK. tick(3)
    pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type==locals.QUIT:
            exit()
        if event.type==locals.KEYDOWN:
            if event.key==pygame.K_q:
            #接收到退出事件后退出程序，按Q
                pygame.mouse.set_visible(True)
                exit()
    screen.blit(background,(0,0))
    if poi==1:
        po="You found the painted eggshell  --  YingMingde"
        p=my_font.render(po,True,(0,0,0))
        screen.blit(p,(0,100))
        er="You win."
        ko=my_font.render(er,True,(0,0,0))
        screen.blit(ko,(150,150))
        pygame.mouse.set_visible(True)
        pygame.display.update()
    #判断胜利
    if dj>=15:
        er="You win."
        ko=my_font.render(er,True,(0,0,0))
        screen.blit(ko,(150,150))
        pygame.mouse.set_visible(True)
        pygame.display.update()
    if yuih==1:
        er="You failed."
        ko=my_font.render(er,True,(0,0,0))
        screen.blit(ko,(150,150))
        pygame.mouse.set_visible(True)
        pygame.display.update()
    pygame.display.update()
    #游戏画面每秒不超过三帧
    FPSCLOCK= pygame.time.Clock();FPSCLOCK. tick(3)
    pygame.mouse.set_visible(False)
