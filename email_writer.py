# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:40:46 2018

@author: Devlin
"""

import listsndicts
import weather
import schedule
import translate
import sunday
import monday
import wednesday
import datetime

####################################################################################################
### Email Data #####################################################################################
### Uses listsndicts.py ############################################################################

sender_one = 'devlin.irwin@gamil.com'
recipient_one = 'pokerbuddy7@gmail.com'
recipient_two = 'devlin.irwin@universalorlando.com'
subject = listsndicts.days_left_in_america() + ' Days Left in America!'

####################################################################################################
###                                                            #####################################
### #       #  #####  #####  #  #  ####    ###   #   #   ###   ### Weekdays - I'm so cool ##########
### #       #  #      #      # #   #   #  #   #  #   #  #      ### Each function prints the ########
###  #  #  #   ###    ###    ##    #   #  #####   # #    ###   ### results of the daily function ###
###  #  #  #   #      #      # #   #   #  #   #    #        #  ### in a legible way ################
###   ## ##    #####  #####  #  #  ####   #   #    #     ###   #####################################
###                                                            #####################################
####################################################################################################
### Uses listsndicts.py sunday.py monday.py wednesday.py       #####################################
####################################################################################################

def get_sunday_text():
    if datetime.date.weekday(datetime.date.today()) == 6:
        sunday_text = "Sunday is Astronomy and Phtography Day!\n\nSunrise: " + sunday.get_sun_info()[0] + "\nSunset: " + sunday.get_sun_info()[1] + "\n\nMoon Illumination: " + sunday.get_moon_info() + "%" + "\n\n" + sunday.get_star_chart() + "\n"
    else:
        sunday_text = "Wrong Day!"
    
    return sunday_text

def get_monday_text():
    if datetime.date.weekday(datetime.date.today()) == 0:
        monday_text = "Monday is Budget and Finance Day!\n\nFord (" + monday.get_stock_data()['Tickers'][1] + "): " + str(monday.get_stock_data()['Prices'][1]) + ", " + str(monday.get_stock_data()['Pct Change'][1]) + "% " + ('up' if monday.get_stock_data()['Pct Change'][1] > 0 else 'down') + " from last week" + "\nComcast (" + monday.get_stock_data()['Tickers'][0] + "): " + str(monday.get_stock_data()['Prices'][0]) + ", " + str(monday.get_stock_data()['Pct Change'][0]) + "% " + ('up' if monday.get_stock_data()['Pct Change'][0] > 0 else 'down') + " from last week"  + "\n"
    else:
        monday_text = "Wrong Day!"
        
    return monday_text

def get_tuesday_text():
    if datetime.date.weekday(datetime.date.today()) == 1:
        tuesday_text = "Tuesday is Fun in the Sun Day!\n\nHere's an activity suggestion: " + listsndicts.fun_in_the_sun_selector() + "\n"
    else:
       tuesday_text = "Wrong Day!"
     
    return tuesday_text

def get_wednesday_text():
    if datetime.date.weekday(datetime.date.today()) == 2:
        wednesday_text = "Wednesday is Coking Day!\n\nFollow this link to a recipe suggestion: " + wednesday.recipe_of_the_day() + "\n"
    else:
        wednesday_text = "Wrong Day!"
       
    return wednesday_text

def get_thursday_text():
    if datetime.date.weekday(datetime.date.today()) == 3:
        thursday_text = "Thursday is Try Something New Day!\n\nHere's a suggestion: " + listsndicts.TSN_Activity[0] + "\n"
    else:
        thursday_text = "Wrong Day!"
       
    return thursday_text

def get_friday_text():
    if datetime.date.weekday(datetime.date.today()) == 4:
        friday_text = "Friday is Programming and Data Analysis Day!\n\nTry looking at Data.Gov for an interesting data set to parse" + "\n"
    else:
        friday_text = "Wrong Day!"
       
    return friday_text

def get_saturday_text():
    if datetime.date.weekday(datetime.date.today()) == 5:
        saturday_text = "Saturday is Gardening Day!\n\nHere's today's garden work: " + listsndicts.Gardening_Timeline[datetime.date.today()] + "\n"
    else:
        saturday_text = "Wrong Day!"
       
    return saturday_text


weekdays = {0: get_monday_text,
            1: get_tuesday_text,
            2: get_wednesday_text,
            3: get_thursday_text,
            4: get_friday_text,
            5: get_saturday_text,
            6: get_sunday_text
            }

daily_text = weekdays[datetime.date.weekday(datetime.date.today())]()

####################################################################################################
### Words of the Day ###############################################################################
### Uses translate.py ##############################################################################

words = translate.translate(translate.word_of_the_day())
language_text = "\n\nWord of the Day: " + words[0] + "\nFrench Translation: " + words[1][0] + "\nGerman Translation: " + words[2][0] + "\n\n"

####################################################################################################
### Schedule #######################################################################################
### Uses schedule.py ###############################################################################

all_days = schedule.get_todays_schedule()['All-Days']
events = schedule.get_todays_schedule()['Events']

if not all_days:
    all_days_text = ''
else:
    all_days_text = "This is what's happening today: " + ', '.join(all_days)

if not events:
    events_text = 'We have a free day today!'
else:
    events_text = "Here is today's schedule: " + ', '.join(events)

####################################################################################################
### Weather ########################################################################################
### Uses weather.py ################################################################################

high = str(weather.get_daily_weather()['Daily High'])
low = str(weather.get_daily_weather()['Daily Low'])
wind_speed = str(weather.get_daily_weather()['Wind Speed'])
weather_conditions = weather.get_daily_weather()['Weather Conditions']

weather_text = "\n\nHere's Today's Forecast:\n" + ", ".join(weather_conditions) + "\nHigh: " + high + "\nLow: " + low + "\nWind Speed: " + wind_speed + " Knots\n"

####################################################################################################
### Putting it all together ########################################################################

daily_update = daily_text + language_text + all_days_text + events_text + weather_text