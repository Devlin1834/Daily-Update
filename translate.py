# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:48:06 2018

@author: Devlin
"""

def word_of_the_day():
    app_id = 'ad769f2c'
    app_key = 'cf2e420fae05d2bd49d11432e5138d21'    
    
    import requests, json, random
    
    language = 'en'
    
    registers = ['Rare', 'Humorous', 'Literary', 'Technical']
    register_select = random.randint(1, len(registers)-1)
    #extar = ?limit=3&offset=0
    
    select_url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/registers=' + registers[register_select]    
    select_r = requests.get(select_url, headers = {'app_id': app_id, 'app_key': app_key})
    
    select_json = json.loads(select_r.text)
    words = [w['word'] for w in select_json['results']]   
    
    word_of_the_day = random.choice(words)
    
    return word_of_the_day
    
def translate(words):
   from googleapiclient.discovery import build

   service = build('translate', 'v2',
            developerKey='AIzaSyChyXFx8546F-ttRwATkccRhq1LR0h1i1M')
   french = service.translations().list(
      source='en',
      target='fr',
      q=words
    ).execute()
  
   german = service.translations().list(
      source='en',
      target='de',
      q=words
    ).execute()
   
   french_words = [f["translatedText"] for f in french["translations"]]
   german_words = [g["translatedText"] for g in german["translations"]]
       
   return [words, french_words, german_words]