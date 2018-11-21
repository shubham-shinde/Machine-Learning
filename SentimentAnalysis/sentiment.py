# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:03:45 2018

@author: sudha
"""
from textblob import TextBlob

text = "Galgotia is a best College"

obj = TextBlob(text)

sentiment = obj.sentiment.polarity