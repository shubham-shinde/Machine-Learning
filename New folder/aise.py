# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:35:21 2018

@author: sudha
"""

from bs4 import BeautifulSoup
htmlf = open('html.html','r')
page = htmlf.read()

soup = BeautifulSoup(page, 'html.parser')

reviews = soup.find_all('p')

positive = 0;
negative = 0;

from textblob import TextBlob

for p in reviews:
    text = p.get_text()
    sentiment = TextBlob(text).sentiment.polarity
    if(sentiment >= 0):
        positive += 1
    else:
        negative += 1

print("Positive Rieview : ",positive)

print("Negative Rieview : ",negative)