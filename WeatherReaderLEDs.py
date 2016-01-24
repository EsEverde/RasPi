import sys
import string
import pywapi
import opc
import time
from random import randint
from datetime import datetime

TimeToUpdate=15 #Update time in min
numLEDs =30 #Init LEDs
MaxLED=64
Strips=5
Map=[[0 for x in range(numLEDs+2)] for x in range(Strips+2)]
client = opc.Client('localhost:7890')


weather_com_result = pywapi.get_weather_from_weather_com('GMXX0053') #Read weather in _____
#weather_com_result = pywapi.get_weather_from_weather_com('WAXX0004')
#weather_com_result = pywapi.get_weather_from_weather_com('RSXX0122')

hour=datetime.now().hour #What time is it? (only hour)
SunsetHour=weather_com_result['forecasts'][0]['sunset']
SunriseHour=weather_com_result['forecasts'][0]['sunrise']
pixels=[ (0,0,0) ] * (MaxLED * Strips)
if len(SunsetHour)>7: #Sunset hour in am/pm
    SunsetHour=str(SunsetHour[0]+SunsetHour[1])
    SunsetHour=int(SunsetHour)
else:
    SunsetHour=int(SunsetHour[0])

SunriseHour=int(SunriseHour[0])

if  hour>SunriseHour and hour<12: #Display greeting
    print "Good morning KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"

elif (hour< SunriseHour)or(hour>12 and hour%12>SunsetHour):
    print "Good evening KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"

else:
    print "Hello KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"

while True: #Main loop

    weather_com_result = pywapi.get_weather_from_weather_com('GMXX0053') #Read weather in Heidelberg
    #weather_com_result = pywapi.get_weather_from_weather_com('WAXX0004')  # ... Windhoek
    #weather_com_result = pywapi.get_weather_from_weather_com('RSXX0122') # ... Yakutsk

    Temp=int(weather_com_result['current_conditions']['temperature'])   #Read out Temp
    Conditions=string.lower(weather_com_result['current_conditions']['text']) #Read out Conditions

    Timeout = time.time() + 60*TimeToUpdate

    Wind=0
    Calm=0
    
    for i in range(0,Strips): #Init Map
        for j in range(0,numLEDs):
            Map[i][j]=randint(1,3)
    
 
    
    if Temp>=10 and Temp<34: # Define colors
        MyColors=[(100+(Temp-10)*6,150-(Temp-10)*4,50),(155+(Temp-10),155,150),(60+Temp-10,60,50)]
    elif Temp<10:
        MyColors=[(100+(Temp-10)*4,150+(Temp-10)*2,50-(Temp-10)*10),(155,155+(Temp-10),150-(Temp-10)),(60,60-(Temp-10)//2,50-(Temp-10))]
    elif Temp>=35:
        MyColors=[(255,0,0),(200,150,150),(80,50,50)]
    
    while time.time() < Timeout: # For the next 15 min
        
        for i in range(0,Strips):
            Map[i][1]=randint(1,3)
        MapAlt=Map
        
        for i in range(1,Strips):
            for j in range(1,numLEDs): #Cloud displacement:
                Switch=randint(0,3+Wind+Calm)  # move to any direction with 1/(4+Wind+Calm) prob
                if Switch==0:
                    MapAlt[i-1][j]=Map[i][j]
                elif Switch==1:
                    MapAlt[i+1][j]=Map[i][j]
                elif Switch==2:
                    MapAlt[i][j-1]=Map[i][j]
                elif Switch>=3 and Switch<=3+Wind: # move upwind with 1/(4+Wind+Calm) + Wind/(4+Wind+Calm)
                    MapAlt[i][j+1]=Map[i][j]
                #else ... Map[i][j]=Map[i][j] # don't move with Calm/(4+Wind+Calm)
        Map=MapAlt
        for i in range(0,Strips):
            for j in range(0,numLEDs):
                pixels[(i)*MaxLED+j] = MyColors[Map[i][j]-1]
            
        client.put_pixels(pixels)
        time.sleep(0.5)

            
                    


