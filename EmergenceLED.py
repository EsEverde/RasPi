import sys
from random import randint
import opc, time

numLEDs =30
MaxLED=64
Strips=5
client = opc.Client('localhost:7890')

Width=20;
Height=60;


MyColors=[(255,0,0),(50,255,150),(30,0,0)]

Map=[[0 for x in range(Height)] for x in range(Width)]
pic=Map
for i in range(1,Width-2):
    for j in range(1,Height-2):
        Map[i][j]=randint(1,3)

while True:
    
    for i in range(1,Width-2):
        pixels=[ (0,0,0) ] * (64 * Strips)
        
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

    pixels=[ (0,0,0) ] * (MaxLED * Strips)
    for i in range(1,Width/4+1):
        for j in range(1,Height/2):
                pixels[(i-1)*MaxLED+j-1] = MyColors[Map[i*3][j*2]-1]

    client.put_pixels(pixels)
    time.sleep(0.5)


