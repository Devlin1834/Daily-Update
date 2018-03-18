# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:45:55 2017

@author: Devlin
"""

import datetime as dt

def fun_in_the_sun_selector():
    import random as rn
    
    FITS_Activities = ['Rock Springs', 'Blue Springs', 'Wekiwa Spings', 'Klondike Beach',
		   'Cross Seminole Trail', 'Bar Street Trail', 'Flagler Trail', 'Space Coast']
    
    selector = rn.randint(0, len(FITS_Activities) - 1)
    
    return FITS_Activities[selector]

TSN_Activity = ['Say yes when you would say no!']


Gardening_Timeline = {dt.date(2018, 2, 17): 'Weed', 
                      dt.date(2018, 2, 24): 'Finish Weeding', 
                      dt.date(2018, 3, 3): 'Water and Fertilize', 
                      dt.date(2018, 3, 10): 'Carrots Germinate', 
                      dt.date(2018, 3, 17): 'Sunflowers Germinate', 
                      dt.date(2018, 3, 24): 'Repot Plants CAREFULY', 
                      dt.date(2018, 3, 31): 'Harvest Radishes',  
                      dt.date(2018, 4, 7): 'Plant Radishes, Batch 2',  
                      dt.date(2018, 4, 14): 'Water and Appreciate Beauty',  
                      dt.date(2018, 4, 21): 'Repot again if necessary',  
                      dt.date(2018, 4, 28): 'Just keep watering',  
                      dt.date(2018, 5, 5): 'Something will happen soon, probably',  
                      dt.date(2018, 5, 12): 'Tomatos, Jalepenos, Bell Pepper, Carrots, and Radishes are ready to Harvest',  
                      dt.date(2018, 5, 19): 'Eggplants are ready to Harvest',  
                      dt.date(2018, 5, 26): 'Sunflowers Bloom',  
                      }   


# Using a List of lists would be more convoluted but would allow me to look up dates by
# milestones. Just a thought

Happy_Thoughts = ['Have a great day everybody!',
                  'Your smile makes my day!',
                  'There is always a silver lining!',
                  'Life ... uh ...finds a way',
                  'Respect is earned but courtesy is given',
                  'Shit happens, no need for blame, just learning',
                  'The journey is more important the destination',
                  'You create your own purpose in life',
                  'It can always get worse',
                  'Everyone wants to be happy']

def days_left_in_america():
    import datetime as dt
    
    today = dt.date.today()
    leaving = dt.date(2018, 6, 4)
    delta = (leaving - today).days
    
    return str(delta)


def activities():
    import datetime as dt
    
    activities = {0: 'Budget and Finance',
                  1: 'Fun in the Sun',
                  2: 'Cooking',
                  3: 'Try Something New',
                  4: 'Programming and Data Analysis',
                  5: 'Gardening',
                  6: 'Photography and Astronomy'}
    
    exercise = {0: 'Strength',
                1: 'Cardio',
                2: 'Strength',
                3: 'Cardio',
                4: 'Strength',
                5: 'Rest',
                6: 'Rest'}

    today = dt.date.today()

    todays_activity = activities[today.weekday()]
    todays_exercise = exercise[today.weekday()]
    
    return [todays_activity, todays_exercise]