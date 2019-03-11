import pygame
from pygame.locals import *
import sys
import math
import os
import random
pygame.init()
width=720
height=405
keys=[False,False,False,False]
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Helicopter")
bg= pygame.image.load('background(720).jpg')
bg_size = bg.get_size()
w,h=bg_size
hpsound= pygame.mixer.music.load('sound/hpsound.mp3')
hcop=[pygame.image.load('separated_frames/helicopter_1.png'),pygame.image.load('separated_frames/helicopter_2.png'),pygame.image.load('separated_frames/helicopter_3.png'),pygame.image.load('separated_frames/helicopter_4.png'),pygame.image.load('separated_frames/helicopter_5.png'),pygame.image.load('separated_frames/helicopter_6.png'),pygame.image.load('separated_frames/helicopter_7.png'),pygame.image.load('separated_frames/helicopter_8.png'),pygame.image.load('separated_frames/cabine.png')]
#bgtree=pygame.image.load('tree.png')
hcb=pygame.image.load('separated_frames/helicopter_back.png')
bgloop= False
hploop= False
start=False
end = False
time = None
qwe=0
FONTs = pygame.font.SysFont("None", 20)
font = pygame.font.SysFont("comicsans", 80)
title = font.render("Copter", 1, (0,200,0))
join = font.render("Press Enter!", 1, (0, 128, 0))
TEXT_COLOR = (0, 0, 0)
start_time = None
bgx=0
bgx1=+w
bgy=0
theClock = pygame.time.Clock()

class downob():
    img = pygame.image.load('rec.png');
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(x,y,width,height)
    def draw(self,screen):
        self.hitbox = (self.x,self.y,self.width,self.height)
        screen.blit(self.img,(self.x,self.y))
    def collide(self,hcbody):
    #(rect[0]= x coordinate,rect[1]=y,rect[2]=width,rect[3]=height)player position and same with hitbox
        if hcbody[0]+hcbody[2]>=self.hitbox[0] and hcbody[0] < self.hitbox[0]+self.hitbox[2]:
            if hcbody[1]+hcbody[3]>self.hitbox[1]:
            #if hcbody[1]>self.hitbox[1]:
                return True
        return False
    
class upob(downob):
    img  =pygame.image.load('rec.png')
    def draw(self,screen): 
        self.hitbox = (self.x,self.y,self.width,self.height)
        screen.blit(self.img,(self.x,self.y))
    def collide(self,hcbody):
        if hcbody[0]+hcbody[2]>=self.hitbox[0] and hcbody[0] < self.hitbox[0]+self.hitbox[2]:
            if hcbody[1]<self.hitbox[3]:
                return True
        return False
class hc():
   
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.v=10
        self.falling=False
        self.o=0
    def draw(self, screen):
        if self.falling:
            if(self.y<300):
                screen.blit(hcop[8], (self.x, self.y))
                self.y+=1
            else:
                screen.blit(hcop[8], (self.x,self.y))
                end =True
        else:
            if(hploop):
                if(self.o<8) and (self.y<300):
                    self.hitbox = (self.x+10,self.y,self.width,self.height)
                    screen.blit(hcop[self.o], (self.x,self.y))
                    self.o+=1
                elif(self.y<300):
                    self.o-=8
                    self.hitbox = (self.x+10,self.y,self.width,self.height)
                    screen.blit(hcop[self.o], (self.x,self.y))
                else:
                    screen.blit(hcop[8], (self.x,self.y))
                    end =True
            else:
                self.hitbox = (self.x+10,self.y,self.width,self.height)
                screen.blit(hcop[1],(50,50))
def redraw():
    cop.draw(screen)
    if not(start):
        screen.blit(title, (width/2 - title.get_width()/2, 100))
        screen.blit(join, (width/2 - join.get_width() / 2, 200))
    if start_time:
        for x in objects:
            x.draw(screen)
        pygame.mixer.music.play(-1)
        time_since_enter = pygame.time.get_ticks() - start_time
        p=time_since_enter/60000
        timer = 'Time: '+str(round(p,2))
        score=int(time_since_enter/10)
        point = 'Score: '+str(score)
        screen.blit(FONTs.render(point, True, TEXT_COLOR), (5, 5))
        screen.blit(FONTs.render(timer, True, TEXT_COLOR), (648, 5))
    else:
        if(end):
            finalscore =int((pygame.time.get_ticks()/10))
            message = 'Score: '+str(finalscore) 
            screen.blit(font.render(message, True,(0,255,0)), (200, 140))
    pygame.display.update()
#upobb=upob(250,0,33,151)
#downobb=downob(300,180,33,151)     
cop=hc(50,50,79,33)
pygame.time.set_timer(USEREVENT+1, 500)
speed=48;
pygame.time.set_timer(USEREVENT+2,random.randrange(2000,3500))
run=1
objects=[]
while run:
    screen.fill(0)
    for obb in objects:
        if obb.collide(cop.hitbox):
            cop.falling=True
            
        obb.x -= 5
        if obb.x<obb.width*-1:
            objects.pop(objects.index(obb))
    if cop.y<300:
        cop.y+=0.5
    else:
        end=True
        bgloop = False
        start_time = None
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=0
            exit(0)
        if event.type == USEREVENT+1:
            speed += 1 
        if event.type == USEREVENT+2:
            r=random.randrange(0,2)
            if r==0:
                objects.append(upob(810,0,33,151))
            else:
                objects.append(downob(810,180,33,151))
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True
                bgloop = True
                hploop = True
                start_time = pygame.time.get_ticks()
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True   
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key==pygame.K_UP:
                keys[2]=False                    
        if keys[0] and cop.x>-5:
            cop.x-=cop.v
        elif keys[1] and cop.x<width-90:
            cop.x+=cop.v
        if keys[2] and cop.y>1:
            cop.y-=cop.v
    if (bgloop):
        bgx1-=5
        bgx-=5
        screen.blit(bg,(bgx,bgy)) 
        screen.blit(bg,(bgx1,bgy))
        if bgx==0:
            bgx1=w
        if bgx1==0:
            bgx=w
    else:
        screen.blit(bg,(0,0))
    redraw()
    theClock.tick(speed)
    run+=1
pygame.quit()
