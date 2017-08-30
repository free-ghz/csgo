#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from random import randint
from random import choice

maxsize = 32 # how many characters in a steam name
safety = 2 # margin

leetl = {
	'a': ['4','/\\'],
	'b': ['6','8'],
	'c': ['☪'],
	'e': ['3','<-'],
	'g': ['9'],
	'i': ['1','!'],
	'j': ['/'],
	'k': ['✂'],
	'l': ['|','|_'],
	'o': ['0','<>', '☢'],
	'P': ['|*'],
	'q': ['♀'],
	's': ['5'],
	't': ['7', '✝'],
	'u': ['V'],
	'v': ['\\/'],
	'x': ['><'],
	'z': ['2'],
	'1': ['I'],
	' ': ['_', ''],
	'0': ['o','O','<>']
}
def leet(inte):
	jo = ""
	for x in xrange(len(inte)):
		if inte[x].lower() in leetl:
			if randint(0,randint(1,5)) == 0:
				jo += choice(leetl[inte[x]])
			else:
				jo += inte[x]
		else:
			jo += inte[x]
	return inte #return jo

# these are displayed in the cs go-font
#♠♥♦♣⌨✏✒✂☢☣↗↘↙↩☸☯✝☦☪☮♀♂Ⓜ☿✈⌛⌚☀☁☂❄☄☎☠☝✌✍❤❣♨☭
working_emoji = ['☭', '♠', '♥', '♦', '♣', '⌨', '✏', '✒', '✂', '☢', '☣', '↗', '↘', '↙', '↩', '☸', '☯', '✝', '☦', '☪', '☮', '♀', '♂', 'Ⓜ', '☿', '✈', '⌛', '⌚', '☀', '☁', '☂', '❄', '☄', '☎', '☠', '☝', '✌', '✍', '❤','❣', '♨']
def decoration(inte):
	a = choice(working_emoji)
	if randint(0,1) == 0:
		b = a
	else:
		b = choice(working_emoji)
	if len(inte) <= maxsize - 6:
		inte = a + b + " " + inte + " " + b + a
	elif len(inte) <= maxsize - 4:
		inte = a + " " + inte + " " + a
	else:
		inte = a + inte + a
	return inte

def apply(name):
	wn = name
	if len(wn) <= maxsize - safety: 
		wn = leet(wn)
	if len(wn) <= maxsize - safety:
		wn = decoration(wn)
		#print("b> " + str(len(wn)))
	return wn

def givefive(amount_lol):
	words = ""
	with open("nounlist.txt") as f:
		words += f.read() + "\n"
	words = words.split("\n")
	output = ""
	for x in xrange(amount_lol):
		ok_nice = apply(choice(words) + " " + choice(words))
		if (len(ok_nice) <= maxsize):
			output += "---     " + ok_nice + "\n"
	return output