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

	words_evil = [("stop cheating", 1), ("cheat", 1), ("fuck", 5), ("heck", 1), ("fucking", 1), ("ass", 3), ("wtf", 3), ("of shit", 2), ("piss", 3), ("worst", 1), ("leave", 1), ("cry", 1), ("stop downloading", 1), ("kick", 3), ("child", 2), ("p12", 1), ("12yo", 1), ("bullshit", 1), ("wurst", 1), ("tu madre", 1), ("toggle", 1), ("VAC", 2), ("vacation", 1), ("russian", 2), ("poland", 1), ("suck", 3), ("lose", 2), ("get rekt", 3), ("git gud", 1), ("bg", 2), ("noob", 5), ("knob", 2), ("n00b", 2), ("newb", 1), ("blyat", 1), ("idiot", 4), ("rekt", 4), ("troll", 2), ("because of you", 1), ("rest of team", 1), ("told you", 1), ("issues", 1)];
	words_good = [("youre good", 1),("nice one", 4),("well jobbed", 1),("thanks", 2),("nice skin", 3),("best round", 1),("master", 1),("well fucked", 1),("nice man", 2),("nice", 5),("fuck yes", 2),("good play", 1),("nice job", 3),("holy shit yes", 2),("well done", 3),("oh yeah", 2),("yes", 1),("dude", 2),("bro", 2),("heck yea", 3),("you did well", 1),("hah!", 1)];
	csgo_words = [("drop", 2),("clutch", 2),("awp mid", 1),("awp long", 1),("awp", 3),("eco", 3),("knife round", 1),("1v1", 3),("shrek", 1),("bomb a", 2),("bomb b", 2),("plant", 4),("dont plant", 5),("afk", 2),("defuse", 3),("dont defuse", 5),("15-15", 1),("16-15", 4),("16-0", 3),("well", 1),("ilu xo", 1),("haha", 5),("youll", 1),("yall better", 1),("its", 2),("were", 1),("im gonna", 1),("you", 3),("buy ak all", 1),("buy kev", 1),("buy awp all", 1),("buy negev", 1),("no", 5),("yes", 2),("rush", 1),("all", 1),("pls", 1),("plz", 4),("sausage", 1),("win the game", 1),("winn the shit", 1),("clan", 2),("EU", 2),("omg", 5),("lmao", 1),("godforsaken", 1),("bro", 3),("dude", 1),("man", 3),("damg", 2),("shjit", 3),("dont step", 2),("shut up", 2),("better", 1),("vodka", 1),("keylogger", 1),("KGB", 1),("aim", 2),("leftist", 1),("dont", 1),("gg", 5),("spray control", 1),("player", 1),("hack", 1),("ace", 6),("sick", 2),("wew", 3),("lad", 1),("smg", 1),("only", 1),("youtube", 1),("oh no", 1),("smh", 2)];

	if nice == True:
		csgo_words += words_good
	else:
		csgo_words += words_evil


	unfurled = []

	output = []


	for word in csgo_words:
		for i in range(word[1]):
			unfurled.append(word[0])

	sent = ""
	# lägg ihop några ord
	storlek = choice([1,1,1,1,1,1,2,2,2,2,3,3,4])
	for x in range(storlek):
		sent = sent + choice(unfurled) + " "
		
	return sent