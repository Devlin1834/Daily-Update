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
    
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/registers=' + registers[register_select]
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    
    words = []
    word_json = json.loads(r.text)
    for w in word_json["results"]:
        words.append(w["word"])
        
    words_of_the_day = []
    for i in range(3):
        words_of_the_day.append(random.choice(words))
    
    return words_of_the_day
    
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
   
   french_words = []
   for f in french["translations"]:
       french_words.append(f["translatedText"])

   german_words = []
   for g in german["translations"]:
       german_words.append(g["translatedText"])
       
   return [words, french_words, german_words]

#if __name__ == '__main__':
#  print(translate(word_of_the_day()))