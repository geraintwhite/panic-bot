#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import difflib
import re
import random
from response_database import *

def matchword(phrase1,phrase2):
    return difflib.SequenceMatcher(None, phrase1, phrase2).ratio()

def phrasefilter(phrase):
    phrase = phrase.replace('hi', 'hello')
    phrase = phrase.replace('hey', 'hello')
    phrase = re.sub('[^A-Za-z0-9\s]+', '', phrase.lower())
    noise_words_set = ['of', 'the', 'at', 'for', 'in', 'and', 'is', 'from', 'are', 'our', 'it', 'its', 'was', 'when', 'how', 'what', 'like', 'whats', 'now', 'panic']
    return ' '.join(w for w in phrase.split() if w.lower() not in noise_words_set)

def getResponse(array):
    return random.choice(array[1:])

class panicBot():
    """create new chatbot instance"""
    def __init__(self):
        self.prevResponse = ''
        self.user = {
            'name': '',
            'age': '',
            'location': ''
        }

    def printLogo(self):
        return intro

    def takeInput(self, message):
        out = ''
        if self.prevResponse in Database[3]:
            response = phrasefilter(message)
            responseType = 1
            for word in response.split(' '):
                if word in badFeel:
                    responseType = 0
                elif word in goodFeel:
                    responseType = 1
            if responseType:
                output = random.choice(goodResponse)
            else:
                output = random.choice(badResponse)
            out += '\n' + output + '\n'
            self.prevResponse = ''
        elif self.prevResponse == (Database[0][1] + ' What is your name?') or self.prevResponse == Database[1][1]:
            name = message
            self.user['name'] = name
            out += '\n' + random.choice(['Hello ' + name, 'Hi ' + name, 'Howdy ' + name]) + '\n'
            self.prevResponse = ''
        elif self.prevResponse == (Database[2][1] + ' How old are you?') or self.prevResponse == Database[5][1]:
            age = message
            self.user['age'] = age
            out += '\n' + 'Awesome, I\'ll remember that.' + '\n'
            self.prevResponse = ''
        elif self.prevResponse == (Database[4][1] + ' Where do you live?'):
            location = message
            self.user['location'] = location
            out += '\n' + 'I\'m sure it\'s lovely there.' + '\n'
            self.prevResponse = ''
        else:
            var = phrasefilter(message)
            vals = []
            for i in range(len(Database)):
                vals.append(matchword(var, Database[i][0]))
            maxVal = [0,0]
            for i in range(len(vals)):
                if vals[i] > maxVal[0]:
                    maxVal[0] = vals[i]
                    maxVal[1] = i
            if maxVal[0] > 0.55:
                if maxVal[1] == 0:
                    if self.user['name'] == '':
                        self.prevResponse = Database[maxVal[1]][1] + ' What is your name?'
                    else:
                        self.prevResponse = Database[maxVal[1]][1]
                elif maxVal[1] == 1:
                    if self.user['name'] == '':
                        self.prevResponse = Database[maxVal[1]][1]
                    else:
                        self.prevResponse = 'Your name is ' + self.user['name']
                elif maxVal[1] == 2:
                    if self.user['age'] == '':
                        self.prevResponse = Database[maxVal[1]][1] + ' How old are you?'
                    else:
                        self.prevResponse = Database[maxVal[1]][1]
                elif maxVal[1] == 4:
                    if self.user['location'] == '':
                        self.prevResponse = Database[maxVal[1]][1] + ' Where do you live?'
                    else:
                        self.prevResponse = Database[maxVal[1]][1]
                elif maxVal[1] == 5:
                    if self.user['age'] == '':
                        self.prevResponse = Database[maxVal[1]][1]
                    else:
                        self.prevResponse = 'You are ' + self.user['age'] + ' years old'
                elif maxVal[1] == 6:
                    if self.user['location'] == '':
                        self.prevResponse = Database[maxVal[1]][1]
                    else:
                        self.prevResponse = 'You live in ' + self.user['location']
                elif maxVal[1] == 7:
                    out += '\nFinding directions ...\n'
                    self.prevResponse = directions
                else:
                    self.prevResponse = getResponse(Database[maxVal[1]])
            else:
                self.prevResponse = random.choice(['Sorry, I don\'t understand', 'I don\'t know what you mean', 'Sorry, I don\'t get that', 'You\'ve lost me there'])
            out += '\n' + self.prevResponse + '\n'
        return out

if __name__ == "__main__":
    print intro
    print logo
    bot = panicBot()
    while True:
        print bot.takeInput(raw_input('> '))
