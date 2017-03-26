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

	sentence_patterns = [
		"dude verb",
		"adj dude",
		"dude adj",
		"profamity direction",
		"profamity dude",
		"object at location"
	]

	dude = ["you", "i", "we", "my team", "this guy", "your mom", "my dude"]

	verb = ["rush", "dont step", "dont", "buy armor", "know", "defuse"]
	verb_bad = ["stink", "suck", "noob", "lose", "play bad", "play like bot"]
	verb_nice = ["win", "did well", "did good", "kill enemies"]

	adj = ["team leader", "afk"]
	adj_bad = ["bad", "lame", "ass", "noob", "newb", "bot", "idiot", "dim", "dipshit"]
	adj_nice = ["nice", "good", "mvp", "not bad", "smart"]

	profamity = ["heck", "shit", "fuck", "flip", "dang", "damn", "fuck", "piss", "bugger"]

	direction = ["off", "here", "away", "out", "outta here"]

	location = ["a", "b", "site", "mid", "long", "spawn"]

	objecto = ["bomb", "ak", "awp", "def kit", "one dude", "a guy", "two guys", "all"]

	# activate
	pattern = choice(sentence_patterns)
	# pronouns
	pattern = pattern.replace("dude", choice(dude))
	# verbs
	if nice:
		pattern = pattern.replace("verb", choice(verb + verb_nice))
	else:
		pattern = pattern.replace("verb", choice(verb + verb_bad))
	# adjectives
	if nice:
		pattern = pattern.replace("adj", choice(adj + adj_nice))
	else:
		pattern = pattern.replace("adj", choice(adj + adj_bad))
	# watch yo profamity
	pattern = pattern.replace("profamity", choice(profamity))
	# direction
	pattern = pattern.replace("direction", choice(direction))
	# object was a keyword
	pattern = pattern.replace("object", choice(objecto))
	# location
	pattern = pattern.replace("location", choice(location))

	# print the mother
	return pattern