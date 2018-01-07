# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:45:55 2017

@author: Devlin
"""

star_chart = 'http://www.heavens-above.com/SkyChart.aspx?lat=28.67&lng=-81.2081&loc=Oviedo&alt=16&tz=EST'

def get_star_chart(save = False):
    import urllib.request
    import datetime as dt
    import re

    # heavans above starts at 7pm and adds 1 each folorwing day at the same time. 
    # the decimal is the fraction of the day that has passed since 7pm yesterday
    # heavans_above_hour = 0.04167
    
    heavans_above_start_night = 58119.16667 # 11:00pm    
    start = dt.date(2017,12,31)
    today = dt.date.today()
    day_count = (today - start).days
    
    heavans_above_time = heavans_above_start_night + day_count
    
    star_chart_url = 'http://www.heavens-above.com/wholeskychart.ashx?lat=28.67&lng=-81.2081&loc=Oviedo&alt=16&tz=EST&size=800&SL=1&SN=1&BW=0&time={}&ecl=0&cb=0'.format(heavans_above_time)
    
    
    if save == True:
        urllib.request.urlretrieve(star_chart_url, re.sub('-', '_', '{}_star_chart.jpeg'.format(today)))
    else:
        return star_chart_url
    

def get_sun_info():
    from bs4 import BeautifulSoup
    import requests
    
    sun_info_url = 'http://www.heavens-above.com/sun.aspx?lat=28.67&lng=-81.2081&loc=Oviedo&alt=16&tz=EST'
    
    soup = BeautifulSoup(requests.get(sun_info_url).text, "lxml")
    script = soup.findAll('span')[7].getText()
    rise = script.find('Sunrise')
    Sunrise = script[rise+10:rise+15]
    sset = script.find('Sunset')
    Sunset = script[sset+9:sset+14]
    
    return Sunrise, Sunset

def get_moon_info():
    from bs4 import BeautifulSoup
    import requests
    
    moon_info_url = 'http://www.heavens-above.com/moon.aspx?lat=28.67&lng=-81.2081&loc=Oviedo&alt=16&tz=EST'
    
    soup = BeautifulSoup(requests.get(moon_info_url).text, "lxml")
    Illumination = soup.findAll('span')[11].getText()
    
    return Illumination