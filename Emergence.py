import sys, pygame
#from pygame import PixelArray, Surface, display, Color, pixelcopy, time
from pygame.locals import *
from datetime import datetime
from random import randint

pygame.init()
Width=100;
Height=150;

DisplaySurf = pygame.display.set_mode((Width, Height),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Emergence!')

MyColors=[(0,100,100),(255,0,100),(255,255,100)]

Map=[[0 for x in range(Height)] for x in range(Width)]
pic=Map
for i in range(1,Width-2):
    for j in range(1,Height-2):
        Map[i][j]=randint(1,3)

while True:
    pygame.event.pump()
    event=pygame.event.wait()
    if event.type==QUIT:
        pygame.quit()
        sys.exit()
    elif event.type==VIDEORESIZE:
        screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
        screen.blit(pygame.transform.scale(pic,event.dict['size']),(0,0))
        pygame.display.flip()

    for i in range(1,Width-2):
        for j in range(1,Height-2):
            HitVec=False
            TheHood=[Map[i-1][j],Map[i+1][j],Map[i+1][j-1],Map[i][j+1]]

            for x in TheHood:
                if x==Map[i][j]%3+1:
                    HitVec=True
            
            if  HitVec:
                Switch=randint(0,3)
                if Switch==0:
                    Map[i-1][j]=Map[i][j]
                elif Switch==1:
                    Map[i+1][j]=Map[i][j]
                elif Switch==2:
                    Map[i][j-1]=Map[i][j]
                elif Switch==3:
                    Map[i][j+1]=Map[i][j]
        
            pixObj = pygame.PixelArray(DisplaySurf)
            pixObj[i][j]=MyColors[Map[i][j]-1]
            del pixObj
    pygame.display.update()

    