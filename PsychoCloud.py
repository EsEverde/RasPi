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
client = opc.Client('localhost:7890')
pixels=[ (255,250,240) ] * (64 * Strips)

while True: #Main loop
    
    for i in range(0,Strips):
        for j in range(0,numLEDs-1):

            #Color1=colorsys.hsv_to_rgb(randint(0,255)/255,1,1)
            Color1=colorsys.hsv_to_rgb(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
            Color1=[x*255 for x in Color1]

            pixels[i*MaxLED+j]= Color1

        client.put_pixels(pixels)
#time.sleep(0.1)

            
                    


