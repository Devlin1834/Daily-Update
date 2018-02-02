# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:32:03 2018

@author: Devlin
"""

def get_daily_weather():
    import json, requests
    
    key = 'b5baaa656031c5b2b3ffa717e549385c'
    locations = ['Oviedo,US']
    
    for place in locations:
        url ='http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(place, key)
        response = requests.get(url)
        
        weather_data = json.loads(response.text)
        
        tmax = round((weather_data['main']['temp_max'] * (9/5)) - 459.67, 1)
        tmin = round((weather_data['main']['temp_min'] * (9/5)) - 459.67, 1)
        weather_cond = [c['description'] for c in weather_data['weather']]
        
        if 'wind' in weather_data.keys():
            wind_speed = weather_data['wind']['speed']
        else:
            wind_speed = 0
        
        all_weather = {"Daily High": tmax,
                       "Daily Low": tmin,
                       "Weather Conditions": weather_cond,
                       "Wind Speed": wind_speed
                       }
        
        return all_weather