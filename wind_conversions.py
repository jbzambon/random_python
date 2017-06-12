# Program to convert meteorological wind direction to
#  u, v components and vice versa
#  Formulae from: http://tornado.sfsu.edu/geosciences/classes/m430/Wind/WindDirection.html
#
# Joseph B. Zambon
# 12 June 2017

# Convert from command line
print 'Feed me a wind speed'
windspeed = raw_input();  windspeed=float(windspeed);
print 'Now feed me a wind direction (met standard = wind FROM)'
met_direction = raw_input();  met_direction=float(met_direction);

# Or uncomment and put whatever you want to convert in here
#windspeed = 10        # Unitless, for reference 1kt = 0.514444m/s
#met_direction = 45    #Degrees

import math

# Meteorological wind direction and speed -> U and V
def met2uv(windspeed,met_direction):
    rad = met_direction * math.pi/180
    u = -windspeed * math.sin(rad); u=round(u,3)
    v = -windspeed * math.cos(rad); v=round(v,3)
    return(u, v)

# U and V -> Meteorological wind direction and speed
def uv2met(u,v):
    windspeed = (u**2 + v**2)**0.5; windspeed=round(windspeed,3)
    met_direction = 180/math.pi * math.atan2(-u,-v)
    is_positive = met_direction >= 0
    met_direction = met_direction if is_positive else met_direction+360
    met_direction = round(met_direction,3)
    return(windspeed,met_direction)

# Convert input to U, V components
u,v=met2uv(windspeed,met_direction)
print 'U: ', u, '     V: ', v

# Convert back for funzies
windspeed,met_direction=uv2met(u,v)
print 'Wind Speed: ', windspeed, '     Meteorological Wind Direction: ', met_direction, u'\N{DEGREE SIGN}'
