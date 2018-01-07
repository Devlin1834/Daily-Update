# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:53:36 2018

@author: Devlin
"""

# Won't Work for Good Friday

def get_stock_data():
    import json, requests, datetime
    stocks = ['CMCSA', 'F']
    key = 'Y82CAW6VQ8VAUZRC'
    prices = []
    weekly_changes = []    
    
    for stock in stocks:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(stock, key)
        response = requests.get(url)
        stock_data = json.loads(response.text)
        pad = stock_data["Time Series (Daily)"] # pad is Previous Available Data
        
        today = datetime.date.today()
        current_stock_date = (today - (datetime.timedelta(today.weekday() + 3))).strftime('%Y-%m-%d')
        previous_stock_date = (today - (datetime.timedelta(today.weekday() + 10))).strftime('%Y-%m-%d')
        
        this_week = pad[current_stock_date]["4. close"]
        prev_week = pad[previous_stock_date]["4. close"]
        
        pct_change = round(((float(this_week) - float(prev_week)) / float(prev_week)) * 100, 2)
        
        prices.append(this_week)
        weekly_changes.append(pct_change)
        
    all_data = {"Tickers": stocks,
                "Prices": prices,
                "Pct Change": weekly_changes
                }
    
    return all_data

get_stock_data()