#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from random import randint
from random import uniform
from random import choice
import string
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

def produce(nice):

	sentences_good = [
		"whats up you fucking mango",
		"well played",
		"you did a good job",
		"that was impressive",
		"it was nice how you did that",
		"i didnt believe that was possible",
		"nice",
		"well clutched my man",
		"fucking a dude",
		"oh shit what a play",
		"oh snap how did you do that",
		"that was impressive of you",
		"good game everyone",
		"have fun my team and enemy team",
		"we win the game",
		"lets do this and get home in time for chow",
		"we do this, and then we go home",
		"gg",
		"well done, impressive",
		"i like your style",
		"nice shoes",
		"nice shot",
		"good shootings dude",
		"are you sure you are not very good? my man you are good",
		"can you teach me how to do that",
		"omg what are your rank?",
		"what is going on. how is this possible",
		"good luck",
		"good luck my friend and dude",
		"you are not my friend, you are my brother, my friend",
		"you are doing fine",
		"good plant dude",
		"whoa, that spray control",
		"hey team i love you",
		"you are good with that weapon",
		"shit you can do it",
		"it is possible",
		"im sorry for not being good enough",
		"haha nice",
		"awesome bro",
		"im proud of each and every one of you",
		"oh shit good game",
		"haha",
		"omg",
		"nice",
		"hehe the other team... am i right",
		"we will win",
		"ok lets do this",
		"im trusting your skill",
		"good skill man",
		"nice plays you did",
		"good round everyone",
		"good game people",
		"awp god",
		"awp good",
		"noscope him with your gun",
		"have a nice evening",
		"it is cold outside but youre warming my heart",
		"nice ak skin",
		":)",
		":D",
		"xD"
	]

	sentences_evil = []	

	sentence_source = [
		"help",
		"please help me i am dying",
		"oh shit here they come",
		"dont step fucking idiot",
		"please press shift noob",
		"where are we",
		"what map is this",
		"i dont know you",
		"ez",
		"dont plant",
		"dont defuse",
		"attack the enemies",
		"let us go b all",
		"time is running up it is time to go to the store",
		"i will need to confiscate all your resources",
		"im hungry",
		"kick me",
		"dont go here",
		"let us have a knife round",
		"come with knife only at long",
		"this place is a shitheap",
		"it will get done",
		"we will plant the bomb",
		"where are you from",
		"i love eating toast",
		"please do your best today",
		"we will win this i believe",
		"it is time for us to get together and fuck off",
		"autonoob",
		"welcome to the space jam",
		"welcome to counter strike global offensive",
		"hello team",
		"hello my enemies and friends",
		"we are gathered here today to kill people over the internet",
		"it is time to go home",
		"when will you stop",
		"sometimes i feel i got to bam bam get away",
		"somebody told me you had a girlfriend",
		"what the heck",
		"what the fuck",
		"great plan dro",
		"you just got naenaed",
		"get up its time to slam jam",
		"*dab*",
		"have you taken your meds today",
		"please salute the flag",
		"this is genuinely helpful",
		"how often do you rotate",
		"please potato a little more often",
		"dont come back",
		"i dont know man",
		"amaze balls"
	]

	wordcounter = {}


	if nice == True:
		sentence_source += sentences_good
	else:
		sentence_source += sentences_evil


	# some preparings
	for i in range(len(sentence_source)):
		for word in sentence_source[i].split(" "):
			if word in wordcounter:
				wordcounter[word]+=1
			else:
				wordcounter[word] = 1
		sentence_source[i] = sentence_source[i] + " _stop_"

	# ok begin
	sentence = choice(sentence_source).split(" ")
	last_index = 0
	output = ""
	latest_word = sentence[last_index]
	# så vi har gjort första ordet
	# fortsätt addera nya ord:
	while latest_word != "_stop_":
		# lägg dit orden vi ska använda!
		output += latest_word + " "
		new_word = sentence[last_index + 1]
		# om det finns fler än en av nästa ord:
		if new_word != "_stop_" and wordcounter[new_word] > 1:
			# hitta alla meningar med ordet i
			temparray = []
			for x in sentence_source:
				if " " + new_word + " " in x:
					temparray += [x]
			# völj en
			sentence = choice(temparray).split(" ")
			# hitta index
			for x in range(len(sentence)):
				if sentence[x] == new_word:
					last_index = x
		else:
			# det finns bara en av denna så vi ökar helt enkelt bara latset_index - 
			# då kommer den bara lägga till nästa ord i samma mening och köra därifrån
			last_index +=1

		# mest logiskt att ha denna först,
		# men om den ligger här så catchas _stop_ av whilen innan den läggs till
		# vilket är bra
		latest_word = sentence[last_index]

	return output



