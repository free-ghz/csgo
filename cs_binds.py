#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from random import randint
from random import uniform
from random import choice
import string
import sentences_a
import sentences_b
import sentences_c
import datetime
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

exec_time = datetime.datetime.now()

# sixey.es for get new file if new file is on sixey.es i mean yeah

#
#	config!!!!
#
#	check these first so it doesnt do anything stupid!!!!!!!!!!!!!!!!!!!!!
#
#
#	ok!!!!!!!
#

# number of buys/talks per key, multiply this by four, that's how many aliases you inject
max_iterations = 420

# where to save the shit to, i like autoexec, you could choose whatever
file_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\autoexec.cfg"

# what keys to use
key_random_buy = "f5"
key_random_cheap = "f6"
key_say_nice_thing = "f7"
key_say_not_nice_thing = "f8"

# this should be true
always_buy_kev = True

# this will always be written to the file. i put my regular autoexec in here.
default = """
// luki sa att jag skulle skriva denna här
// to do with networks
rate "687500"

//ok detta är bra binds
bind f1 "buy tec9"
bind f2 "buy vest;buy defuser;buy vesthelm"
bind f3 "buy vest;buy ak47;buy defuser;buy vesthelm"
bind f4 "buy vest;buy mp9;buy mac10"

// scout button
bind f9 "buy ssg08;buy awp;buy vest;buy vesthelm"

//ok nu är resten generated
"""

airlines = 'echo "thank you for flying with idiot airlines! ' + str(exec_time) + '"'
default += airlines

#
#
#   v2.3 (26/3 17)
#		* fixed bug "sg008" --> "ssg08"
#		* made it echo generation time so you know if it's fresh
#		* removed the mysql thingy, fuck 40 sec generation time
#		* f7: more trashy than f8
#		* maybe ill put the thing on github hehe
#	v2.2 (04/3 17)
#		* added new generation mode -> shit requires mysql now
#		* no longer distinguishing between nice & naughty
#	v2.1
#		* redid generation of expensive buy so it gives you more of a complete loadout to play with
#	v2.0
#		* more bullshit generation algorithms
#		* kinda distinguishing between nice and naughty things to say
#		* config the keys
#		* a mode for only buying cheaper items (around $2000 max)
#		* flag for always buying kev
#		* now tries to buy both m4's for example
#

pistol =  ["glock; buy hkp2000","p250","elite","deagle","tec9"]
smg =  ["xm1014","mag7","ssg08","awp","ak47","sg556;buy aug","famas; buy galilar","m4a1; buy m4a1_silencer","scar20; buy g3sg1"]
smg_cheap  =  ["mp9;buy mac10","mp7","p90","bizon","ump45","nova","mag7","sawedoff"]
nades =  ["hegrenade","flashbang","smokegrenade","decoy","molotov","incgrenade"]
thing =  ["defuser","vesthelm"]
everything = [pistol, smg, nades, thing]

if not always_buy_kev:
	thing = thing + ["vest"]

#
#	funktion för att emulera dålig skrivning
#

def wonk(text):
	text = text.strip()
	# kanske lite random mellanslag
	if randint(0,4) == 1:
		for x in range(randint(1,2)):
			where = randint(0,len(text))
			text = text[:where] + " " + text[where:]
	# kanske ett komma
	if randint(0,8) == 1:
		where = randint(0,len(text))
		text = text[:where] + "," + text[where:]
	# kanske ett apostrophy
	if randint(0,16) == 1:
		where = randint(0,len(text))
		text = text[:where] + "'" + text[where:]
	# extra letter
	if randint(0,2) == 1:
		where = randint(0,len(text))
		text = text[:where] + choice(string.letters.lower()) + text[where:]
	# remove letter
	if randint(0,3) == 1:
		where = randint(2,len(text))
		text = text[:where-1] + text[where:]
	# kanske utropstecken
	if randint(0,3) == 1:
		text = text + ("!" * randint(1,9))

	return text

output = []

#
#	generera vapenbinds
#

default += "\nbind " + key_random_buy + " bindknapp\nalias bindknapp a0\n"

for i in range(max_iterations):
	# maybe a big gun (2/3)
	slot1 = randint(0,3)
	# if a big gun, maybe a small. if no big, always a small gun
	if slot1 > 0:
		slot2 = randint(0,2)
	else:
		slot2 = 1
	# amount of grenades
	slot3 = choice([0,0,0,0,1,1,1,2,3])

	#ok make gun
	# vest > pistol > cool gun > etc
	sent = "alias a" + str(i) + " \""
	if always_buy_kev:
		sent += "buy vest;"
	if slot2 > 0:
		sent = sent + "buy " + choice(pistol) + ";"
	if slot1 > 0:
		sent = sent + "buy " + choice(smg) + ";"
	for x in range(slot3):
		sent = sent + "buy " + choice(nades) + ";"
	# alltid bra va
	sent = sent + "buy defuser;buy vesthelm;"
	if i == max_iterations-1:
		sent = sent + "alias bindknapp a0\""
	else:
		sent = sent + "alias bindknapp a" + str(i+1) + "\""
	output.append(sent)

#
#	generera cheap binds
#

default += "bind " + key_random_cheap + " cheapknapp\nalias cheapknapp c0\n"

for i in range(max_iterations):
	choices = smg_cheap + pistol
	sent = "alias c" + str(i) + " \"buy "
	if always_buy_kev:
		sent += "vest;buy "
	sent += choice(choices)
	if i == max_iterations-1:
		sent = sent + ";alias cheapknapp c0\""
	else:
		sent = sent + ";alias cheapknapp c" + str(i+1) + "\""
	output.append(sent)

#
#	generera bullshit-talk
#

default += "bind " + key_say_nice_thing + " bindsnack\nalias bindsnack b0\n"

for i in range(max_iterations):
	whichform = randint(0,3)
	if whichform == 0:
		sent = wonk(wonk(wonk(sentences_a.produce(False)) + choice(" haha, hehe".split(","))))
	elif whichform == 1:
		sent = wonk(wonk(sentences_b.produce(False)) + choice(" haha, hehe".split(",")))
	else:
		sent = wonk(wonk(sentences_c.produce(False)) + choice(" haha, hehe".split(",")))
	
	if i == max_iterations-1:
		output.append("alias b" + str(i) + " \"say " + sent + ";alias bindsnack b0\"")	
	else:
		output.append("alias b" + str(i) + " \"say " + sent + ";alias bindsnack b"+ str(i+1) + "\"")

#
#	generera ~evil  talk
#

default += "bind " + key_say_not_nice_thing + " evilsnack\nalias evilsnack e0\n"

for i in range(max_iterations):
	whichform = randint(0,3)
	if whichform == 0:
		sent = wonk(sentences_a.produce(False))
	elif whichform == 1:
		sent = wonk(sentences_b.produce(False))
	else:
		sent = wonk(sentences_c.produce(False))
	
	if i == max_iterations-1:
		output.append("alias e" + str(i) + " \"say " + sent + ";alias evilsnack e0\"")	
	else:
		output.append("alias e" + str(i) + " \"say " + sent + ";alias evilsnack e"+ str(i+1) + "\"")

#
#	ok thats mostly it. print to file!
#

output.append("\n\n")

target = open(file_path, 'w')
target.write(default + "\n".join(output))
target.close()

# C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg