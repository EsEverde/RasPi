from __future__ import division
import sys
import string
import opc
import time
import colorsys
from random import randint
from datetime import datetime


TimeToUpdate=15 #Update time in min
numLEDs =30 #Init LEDs
MaxLED=64
Strips=5
Map=[[0 for x in range(numLEDs+2)] for x in range(Strips+2)]
client = opc.Client('localhost:7890')

while True: #Main loop
    
    #else ... Map[i][j]=Map[i][j] # don't move with Calm/(4+Wind+Calm)
    for k in range(0,255):
        pixels=[ (255,255,255) ] * (64 * Strips)

        for i in range(0,Strips):
            for j in range(0,numLEDs):
                    
                Color1=colorsys.hsv_to_rgb((k+j*4)%255/255,1,1-1/Strips*i)
                Color1=[x*255 for x in Color1]

                    #Color2=colorsys.hsv_to_rgb(1/numLEDs*(j+15)%numLEDs,1,1/10*k*2)
                    #Color2=[x*255 for x in Color2]

                pixels[i*MaxLED+j]= Color1

            client.put_pixels(pixels)
            time.sleep(0.05)

            
                    


