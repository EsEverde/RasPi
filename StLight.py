import sys
import opc
numLEDs =30 #Init LEDs
MaxLED=64
Strips=5
client = opc.Client('localhost:7890')
pixels=[ (255,250,240) ] * (64 * Strips)

client.put_pixels(pixels)
time.sleep(0.1)
client.put_pixels(pixels)




