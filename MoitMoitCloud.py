#from __future__ import division
import sys
import opc
import time
import colorsys
from random import randint


numLEDs =30 #Init LEDs
MaxLED=64
Strips=5
client = opc.Client('localhost:7890')
pixels=[ (255,250,240) ] * (MaxLED * Strips)
Color1=colorsys.hsv_to_rgb(0.05,1,1)
Color2=colorsys.hsv_to_rgb(0.8,1,1)
Color1=[x*255 for x in Color1]
Color2=[x*255 for x in Color2]

while True: #Main loop
    
    for j in range(0,numLEDs):
        for i in range(0,Strips):
            pixels[i*MaxLED+j]= Color1
            pixels[(i*MaxLED+j+(numLEDs/2))%(numLEDs*Strips)]= Color2

        client.put_pixels(pixels)
    time.sleep(0.8)

            
                    


