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
def hsv2rgb(h,s,v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
Color1=hsv2rgb(0.6,0,0.25)
Color2=(218,165,32)

while True: #Main loop
    
    for j in range(0,numLEDs):
        for i in range(0,Strips):
            pixels[i*MaxLED+j]= Color1
            pixels[(i*MaxLED+j+(numLEDs))%(MaxLED*Strips)]= Color2

        client.put_pixels(pixels)
        time.sleep(0.5)