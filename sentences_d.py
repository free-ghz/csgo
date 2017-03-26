#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from pprint import pprint
from random import randint
from random import uniform
from random import choice
import string
import MySQLdb #apt-get install python-mysqldb


def gimme_word(ohshit):
	wheel = []
	for candidate in ohshit:
		times = candidate[3]
		word = candidate[2]
		addition = [word for x in xrange(times)]
		wheel += addition
	return choice(wheel)

def gimme_word2(ohshit):
	wheel = []
	for candidate in ohshit:
		times = candidate[4]
		word = candidate[3]
		addition = [word for x in xrange(times)]
		wheel += addition
	return choice(wheel)

def gimme_word3(ohshit):
	wheel = []
	for candidate in ohshit:
		times = candidate[5]
		word = candidate[4]
		addition = [word for x in xrange(times)]
		wheel += addition
	return choice(wheel)


def generate():
# config

	letter4letter = True

	# no longer config anymore!

	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="",  # your password
	                     db="cs_go")
	cursor = db.cursor()

	if letter4letter == True:
		begin_token = "/"
		end_token = "!"
		joiner = ""
	else:
		begin_token = "@s"
		end_token = "@e"
		joiner = " "

	word1 = begin_token
	sentence = []
	# ok FIRST add the first word!
	cool_query = "SELECT * FROM `two` WHERE ord_a = '"+word1+"'"
	cursor.execute(cool_query)
	candidates = cursor.fetchall()
	word2 = gimme_word(candidates)
	if not word2 == end_token:
		sentence.append(word2)

	# then do the second!
	cool_query = "SELECT * FROM `three` WHERE ord_a = '"+word1+"' and ord_b = '"+word2+"'"
	cursor.execute(cool_query)
	candidates = cursor.fetchall()
	word3 = gimme_word2(candidates)
	if not word3 == end_token:
		sentence.append(word3)

	# then do the REST!
	while not word3 == end_token:
		cool_query = "SELECT * FROM `four` WHERE ord_a = '"+word1+"' and ord_b = '"+word2+"' and ord_c = '"+word3+"'"
		cursor.execute(cool_query)
		candidates = cursor.fetchall()
		word4 = gimme_word3(candidates)
		if not word4 == end_token:
			sentence.append(word4)
		word1 = word2
		word2 = word3
		word3 = word4





	final = joiner.join(sentence)
	db.close() # databasen ligger fan på raspin
	return final
