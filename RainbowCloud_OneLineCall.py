from __future__ import division
import sys
import string
import opc
import time
import colorsys
import argparse
from random import randint
from datetime import datetime

 
TimeToUpdate=15 #Update time in min
numLEDs =30 #Init LEDs
MaxLED=64
Strips=5
Map=[[0 for x in range(numLEDs+2)] for x in range(Strips+2)]
client = opc.Client('localhost:7890')

#RangeMin=input("RangeMin:")
#RangeMax=input("RangeMax:")
#Saturation=input("Saturation:")

def enlighten(RangeMin, RangeMax, Saturation):	
	while True: #Main loop
    	
    	#else ... Map[i][j]=Map[i][j] # don't move with Calm/(4+Wind+Calm)
    		for k in range(1,255):
        		pixels=[ (255,255,255) ] * (64 * Strips)
		
			for i in range(0,Strips):
    				for j in range(0,numLEDs):
            			
        				Color1=colorsys.hsv_to_rgb((RangeMin+k+(RangeMax-RangeMin)/numLEDs*j+(RangeMax-RangeMin)/Strips*i)%255/255,Saturation/255,1)
        				Color1=[x*255 for x in Color1]
            				#Color2=colorsys.hsv_to_rgb(1/numLEDs*(j+15)%numLEDs,1,1/10*k*2)
            				#Color2=[x*255 for x in Color2]
			
        				pixels[i*MaxLED+j]= Color1
			
			client.put_pixels(pixels)
			time.sleep(1.275/(RangeMax-RangeMin))
				
if __name__ == '__main__':
    if ( len(sys.argv) == 4):

        RangeMin = int(sys.argv[1]) 
        RangeMax = int(sys.argv[2])
        Saturation = int(sys.argv[3])

        print "Enlightening you with \n", "RangeMin ", RangeMin, "\n RangeMax ", RangeMax, "\n Saturation ", Saturation
        enlighten(RangeMin, RangeMax, Saturation)

    else:
        print "USAGE: RainbowCloud.py RangeMin RangeMax Saturation"
        sys.exit(10)

