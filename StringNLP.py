#!/usr/bin/env python3.8
import nltk

string = 'TestingTestingTestingTestingTestingTesting'
tokens = nltk.word_tokenize(string)
tagged = nltk.pos_tag(tokens)
tagged[0:6]

print(tokens)
