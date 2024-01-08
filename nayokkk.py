from random import randint
from tkinter import messagebox
import pygame
from pygame import mixer
pygame.init()

#-----------------------------Try Exception zone-----------------------------#
try:
    f = open("highscore.csv")
    font = pygame.font.Font('Minecraft.ttf',24)
    gotfishsound = mixer.Sound("pop.wav")
    imgnamelist = ['pause.jpg','bg.png','wave.png','clock.png','fisher1.png','fisher2.png','f1.png','f2.png','f3.png','f4.png','f5.png',
                    'heart.png']
    for i in range(12):
        image = pygame.image.load(imgnamelist[i])  

except IOError:
    messagebox.showinfo("IO Error","Cloudn't run the program because of file missing")
    pygame.quit()
    quit() 

#-----------------------------Display setting zone-----------------------------#
pygame.display.set_caption('Set Sail: ตกปลาพัฒนาชาติ')
surface = pygame.display.set_mode((600,600))
Icon = pygame.image.load('heart.png'); pygame.display.set_icon(Icon)


#-----------------------------Variable zone-----------------------------#
#background import
pausebg = pygame.image.load('pause.jpg')
imgbg = pygame.image.load('bg.png')
imgwave = pygame.image.load('wave.png')
imgclock = pygame.image.load('clock.png')

#playing or go restarting
played = True
re = False

#numbers increase / decrease (score, time count)
score = 0
tc = 1200       #time cpunt : เลขที่เอาไว้ลบ เอาไปใช้กับเวลา สุ่มเลขเอา สุ่มจนท้อแล้วค่ะอาจารย์
tcs = 112       #time count show : ตอนแรกอยากได้ 120 แต่จริงๆแล้ว 112 ก็ดีเหมือนกัน
tx = 282        #time's text position(แกน x) : พอเวลามันลงลงเรื่อย ๆ แล้วมันไม่กลางเลยตั้งตัวแปรตัวนี้ขึ้นมา

#import font sound
font = pygame.font.Font('Minecraft.ttf',24)
gotfishsound = mixer.Sound("pop.wav")


#player variable (position,animation,move,image)
player = [pygame.image.load('fisher1.png'),
        pygame.image.load('fisher2.png')]
pa=0                    #'pa' from 'player animate'
x = 250                 #ตำแหน่งเริ่มต้นในแกน x
y = 125                 #ตำแหน่งเริ่มต้นในแกน y
move_right = False
move_left = False

#1st fish variable

fish1 = [pygame.image.load('f1.png'),
        pygame.image.load('f2.png'),
        pygame.image.load('f3.png'),
        pygame.image.load('f4.png'),
        pygame.image.load('f5.png')]
fr1=randint(0,4)                     #fish type random
fishrect1 = fish1[fr1].get_rect()
fishrect1.x = 600                    #fish x
fishrect1.y = randint(300,450)       #fish y since



#2nd fish variable
fish2 = [pygame.transform.flip(fish1[0], True, False),
        pygame.transform.flip(fish1[1], True, False),
        pygame.transform.flip(fish1[2], True, False),
        pygame.transform.flip(fish1[3], True, False),
        pygame.transform.flip(fish1[4], True, False)]
fr2 = randint(0,4)                  #fish type random
fishrect2 = fish2[fr2].get_rect()
fishrect2.x = 0                     #fish x
fishrect2.y = randint(300,450)      #fish y since


#bait variable
yelh = pygame.image.load('bait.png')
yelhrect = yelh.get_rect()          #เหมือนสร้างกรอบรอบรูป
yelhrect.y = y+100
yelhrect.x = x+25
fished = False
draw = True                         #หย่อนเบ็ด

#-----------------------------Function zone-----------------------------#

def fishmoving():
    global fishrect1
    global fr1
    fishrect1.x = fishrect1.x - 2
    if fishrect1.x < -100:
        fishrect1.x = randint(600,700)
        fishrect1.y = randint(300,450)
        fr1 = randint(0,4)
    
    global fishrect2
    global fr2
    fishrect2.x = fishrect2.x + 2
    if fishrect2.x > 700:
        fishrect2.x = randint(-100,-50)
        fishrect2.y = randint(300,450)
        fr2 = randint(0,4)

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        surface.blit(pausebg,(0,0))
        pygame.display.update()

def restart():

    re = True
    global score, tcs, x, tx, fishrect1, fishrect2

    while re:
        #เปิดตลอดตอนเล่นเกม ไฟล์ csv จะได้อัพเดตให้เห็นได้ตลอดถ้ามีการทำลายสถิติ
        with open("highscore.csv","r",encoding="utf-8") as f:
            hs=f.read()
            highscore = int(hs)

        highscoretext = font.render('Highscore : {}'.format(highscore), True, (0,0,0), None)
        scoretext = font.render('Score : {}'.format(score), True, (0,0,0), None)
        wannagotext = font.render('press R to restart', True, (0,0,0), None)
        nicetext = font.render('Nice try bro !!', True, (255,255,255), None)
    
        #background image
        surface.fill((65,105,225))
        surface.blit(imgbg,(0,0))
        surface.blit(imgwave,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:  #press button
                if event.key == pygame.K_r:
                    score = 0
                    tcs = 112
                    x = 250
                    tx = 282
                    fishrect1.x = randint(600,700)
                    fishrect1.y = randint(300,450)
                    fishrect2.x = randint(600,700)
                    fishrect2.y = randint(300,450)
                    re = False
                    
        surface.blit(nicetext,(220,100))
        surface.blit(highscoretext,(200,320))
        surface.blit(scoretext,(250,350))
        surface.blit(wannagotext,(190,380))
        pygame.display.update()

#-----------------------------On game zone-----------------------------#

while played:
    #เปิดตลอดตอนเล่นเกม ไฟล์จะได้อัพเดตให้เห็นได้ตลอดถ้ามีการทำลายสถิติ
    with open("highscore.csv","r",encoding="utf-8") as f:
        hs=f.read()
        highscore = int(hs)
    if score > highscore:
        with open("highscore.csv","w",encoding="utf-8") as f:
            s=str(score)
            f.write(s)


    highscoretext = font.render('Highscore : {}'.format(highscore), True, (0,0,0), None)
    scoretext = font.render('Score : {}'.format(score), True, (0,0,0), None)
    timetext = font.render('{}'.format(tcs), True, (0,0,0), None)
    ptext = font.render('P-Pause', True, (0,0,0), None)
    
    #background image
    surface.fill((255,255,255))
    surface.blit(imgbg,(0,0))
    surface.blit(imgclock,(273,3)) #x=273, y=3 so it will be center

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:  #press button
            if event.key == pygame.K_d:
                pa=0
                move_right = True
            if event.key == pygame.K_a:
                pa=1
                move_left = True
            if event.key == pygame.K_s:
                fished = True
                draw = True
                yelhrect.y=y+100        #เพื่อความสวยงาม
                yelhrect.x=x+25         #เพื่อความสวยงามเหมือนกัน
            if event.key == pygame.K_p:
                pause()

        elif event.type == pygame.KEYUP:    #unpress button
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False

    if (move_right)and x < 500:
        x = x + 3
    if (move_left)and x > 1:
        x = x - 3
        
    if fished and yelhrect.y < 500:           #collision
        yelhrect.y = yelhrect.y + 4
        move_left = False
        move_right = False
        
        surface.blit(yelh, yelhrect)

        #หย่อนเบ็ด
        dy = yelhrect.y
        if draw and dy <= 500:  #เริ่มที่ x คือ ตำแหน่งผู้เล่น, y ก็ตำแหน่งเดียวกับไอเบ็ด บวกเลขไปให้มันตรงเฉยๆ
            pygame.draw.line(surface, (0,0,0), (x+40 ,y+100 ), (x+40,yelhrect.y), 1)
            dy = dy + 4
            if dy > 500:
                draw = False
                dy = y

        #ถ้าความเป็นไทยชนปลา(ที่โดนสร้างกรอบไว้แล้ว) โดนแม่เล่น;-; ได้คับๆ
        #ใช้ for i ดีปะวะ แต่ขก.แก้แล้วอะ #ทำไม่ทันแล้วช่วยด้วย
        if yelhrect.colliderect(fishrect1):
            pygame.draw.rect(surface, (255,0,0), yelhrect, 4) #ขึ้นกรอบแดงถ้าชน
            gotfishsound.play()
            if fr1 == 0 or fr1 == 1:
                score = score + 10
            elif fr1 == 2:
                score = score - 50 
            elif fr1 == 3:
                score = score + 5
            elif fr1 == 4:
                score = score + 100
            fishrect1.x = randint(600,700)
            fishrect1.y = randint(300,450)
            fr1 = randint(0,4)
            fished = False
        
        if yelhrect.colliderect(fishrect2):
            pygame.draw.rect(surface, (255,0,0), yelhrect, 4) #ขึ้นกรอบแดงถ้าชน
            gotfishsound.play()
            if fr2 == 0 or fr2 == 1:
                score = score + 10
            elif fr2 == 2:
                score = score - 50
            elif fr2 == 3:
                score = score + 5
            elif fr2 == 4:
                score = score + 100
            fishrect2.x = randint(600,700)
            fishrect2.y = randint(300,450)
            fr2 = randint(0,4)
            fished = False
        
        if score < 0:
            score = 0

    fishmoving()

    #tc #แก้โค้ดจับเวลา
    tc = tc - 1         #ลขเลขใหญ่ไป ตั้งไว้เยอะ ๆ
    if tcs == 120:
            tx = 282
    if tc % 60 == 0:    #ม้อดเลขเล็ก ถ้าตรงกันก็ลบไปเรื่อยๆ
        tcs = tcs-1     #ลบเวลาไปเรื่อยๆ
        if tcs < 100:
            tx = 287
        if tcs < 10:
            tx = 292
        if tcs < 0:
            move_right = False
            move_left = False
            restart()   #จบเกมแล้ว
        

    #text render
    surface.blit(highscoretext,(20,10))
    surface.blit(scoretext,(20,40))
    surface.blit(timetext,(tx,20))
    surface.blit(ptext,(472,20))

    #picture render รูปที่ควรจะอยู่ด้านบน
    surface.blit(fish1[fr1],fishrect1)
    surface.blit(fish2[fr2],fishrect2)
    surface.blit(player[pa],(x,y))
    surface.blit(imgwave,(0,0))
    pygame.display.update()
