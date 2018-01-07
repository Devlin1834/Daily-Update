# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:45:55 2017

@author: Devlin
"""

def recipe_of_the_day():
    import random as rn
    
    ROTD = rn.randint(1, 45284)
    
    return 'http://www.reciperoulette.tv/#{}'.format(ROTD)
