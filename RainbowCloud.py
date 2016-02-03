from __future__ import division
import sys
import string
import opc
import time
import colorsys
import argparse
from random import randint
from datetime import datetime

def RainbowCloud(RangeMin,RangeMax):
 
 
    TimeToUpdate=15 #Update time in min
    numLEDs =30 #Init LEDs
    MaxLED=64
    Strips=5
    Map=[[0 for x in range(numLEDs+2)] for x in range(Strips+2)]
    client = opc.Client('localhost:7890')

    while True: #Main loop
    
        #else ... Map[i][j]=Map[i][j] # don't move with Calm/(4+Wind+Calm)
        for k in range(RangeMin,RangeMax):
            pixels=[ (255,255,255) ] * (64 * Strips)

            for i in range(0,Strips):
                for j in range(0,numLEDs):
                    
                    Color1=colorsys.hsv_to_rgb((k+(RangeMax-RangeMin)/numLEDs*j+(RangeMax-RangeMin)/Strips*i)%(RangeMax-RangeMin)/255,1,1)
                    Color1=[x*255 for x in Color1]

                    #Color2=colorsys.hsv_to_rgb(1/numLEDs*(j+15)%numLEDs,1,1/10*k*2)
                    #Color2=[x*255 for x in Color2]

                    pixels[i*MaxLED+j]= Color1

            client.put_pixels(pixels)
            time.sleep(0.005)

parser = argparse.ArgumentParser(description='Rainbow CLoud with HueValues between Input 1 and Input 2')
parser.add_argument('integers', metavar='N', type=int, nargs='2', help='Value 1 anad 2 between 0 and 255')
args = parser.parse_args()

RainbowCloud(args(0),args(1))
