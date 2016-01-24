import sys
import string
import pywapi
from datetime import datetime


weather_com_result = pywapi.get_weather_from_weather_com('GMXX0053')
#weather_com_result = pywapi.get_weather_from_weather_com('MAXX0002')

hour=datetime.now().hour
SunsetHour=weather_com_result['forecasts'][0]['sunset']
SunriseHour=weather_com_result['forecasts'][0]['sunrise']

if len(SunsetHour)>7:
    SunsetHour=str(SunsetHour[0]+SunsetHour[1])
    SunsetHour=int(SunsetHour)
else:
    SunsetHour=int(SunsetHour[0])

SunriseHour=int(SunriseHour[0])

if  hour>SunriseHour and hour<12:
    print "Good morning KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"

elif (hour< SunriseHour)or(hour>12 and hour%12>SunsetHour):
    print "Good evening KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"

else:
    print "Hello KokatsuPi, it is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Heidelberg.\n\n"
