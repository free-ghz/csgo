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

#
#	config
#

max_iterations = 420


file_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\autoexec.cfg"

#
#	lite data typ, mess with these om du vill
#

pistol =  ["glock","hkp2000","p250","elite","deagle","tec9","tec9"]
smg =  ["mp9","mac10","mp7","p90","bizon","ump45","nova","xm1014","mag7","sawedoff","sg008","awp","ak47","galilar","sg556","g3sg1","famas","m4a1","m4a1-s","aug","scar20"]
nades =  ["hegrenade","flashbang","smokegrenade","decoy","molotov","incgrenade"]
thing =  ["defuser","vest","vesthelm"]
everything = [pistol, smg, nades, thing]

default = "// luki sa att jag skulle skriva denna här\n// to do with networks\nrate \"687500\"\n//ok detta är bra binds\n"
default += "bind f1 \"buy tec9\"\nbind f2 \"buy vest;buy defuser;buy vesthelm\"\nbind f3 \"buy vest;buy ak47;buy defuser;buy vesthelm\"\nbind f4 \"buy vest;buy mp7\"\n//ok nu är resten generated\n"

csgo_words = [("HACK", 1), ("hack", 1), ("stop cheating", 1), ("cheat", 1), ("toggle", 1), ("VAC", 1), ("vacation", 1), ("fuck", 1),("heck", 2),("fucking", 1),("ass", 3),("damg", 2),("shjit", 2),("bullshit",  1),("dont step", 1),("shut up", 1),("youre good", 1),("nice one", 2),("well jobbed", 1),("thanks", 1),("bro", 2),("dude", 2),("man", 2),("wtf", 2),("omg", 2),("lmao", 1),("godforsaken", 1),("of shit", 2),("piss", 3),("win the agme", 2),("winn the shit", 2),("clan", 1),("worst", 1),("leave", 1),("pls", 2),("plz", 1),("wurst", 1),("sausage", 1),("cry", 1),("p12", 1),("12yo", 1),("russian", 1),("poland", 1),("buy ak all", 1),("buy kev", 1),("buy awp all", 1),("buy negev", 1),("no", 2),("yes", 1),("rush", 2),("all", 1),("nice skin", 1),("suck", 1),("lose", 1),("get rekt", 1),("git gud", 1),("best round", 1),("gg", 3),("bg", 1),("noob", 3),("knob", 1),("n00b", 1),("newb", 1),("youll", 2),("yall better", 2),("its", 2),("were", 1),("im gonna", 1),("you" , 2),("SUKA", 1),("blyat", 1),("idiot", 2),("master", 1),("player", 1),("ace", 2),("bomb a", 1),("bomb b", 1),("plant", 2),("dont plant", 2),("afk", 2),("defuse", 2),("dont defuse", 3),("15-15", 1),("16-15", 2),("16-0", 1),("good play", 3),("nice job", 3),("hopy shit yes", 3),("well done", 3),("you did well", 3),("ilu xo", 1),("haha", 2),("well fucked", 1),("tu mandre", 1),("1v1", 2),("shrek", 2),("rekt", 2),("nice man", 2),("kick", 2),("clutch", 2),("awp mid", 1),("awp long", 1),("awp", 1),("eco", 2),("knife round", 1),("fuck yes", 2)]
unfurled = []

output = []

#
#	generera vapenbinds
#

default += "bind f5 bindknapp\nalias bindknapp a0\n"

for i in range(max_iterations):
	clean = [True, True, True, True]
	sent = "alias a" + str(i) + " \"buy "
	prim_slot = randint(0,3)
	clean[prim_slot] = False
	sent = sent + choice(everything[prim_slot])
	# mer än en?
	for kek in range(randint(0,3)):
		while True:
			ny_slot = randint(0,3)
			if clean[ny_slot] == True:
				break
		clean[ny_slot] = False
		sent = sent + ";buy " + choice(everything[ny_slot])
	if i == max_iterations-1:
		sent = sent + ";alias bindknapp a0\""
	else:
		sent = sent + ";alias bindknapp a" + str(i+1) + "\""
	output.append(sent)

#
#	generera snackbinds
#

default += "bind f6 bindsnack\nalias bindsnack b0\n"

for word in csgo_words:
	for i in range(word[1]):
		unfurled.append(word[0])

for i in range(max_iterations):
	sent = ""
	# lägg ihop några ord
	storlek = choice([1,1,1,1,1,1,2,2,2,2,3,3,4])
	for x in range(storlek):
		sent = sent + choice(unfurled) + " "
	sent = sent.strip()
	# kanske lite random mellanslag
	for x in range(choice([0,0,0,0,0,0,1,1,2,3,4])):
		where = randint(0,len(sent))
		sent = sent[:where] + " " + sent[where:]
	# kanske ett komma
	if randint(0,5) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + "," + sent[where:]
	# kanske ett apostrophy
	if randint(0,4) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + "'" + sent[where:]
	if randint(0,3) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + choice(string.letters) + sent[where:]
	# kanske utropstecken
	if storlek < 3 and randint(0,2) == 1:
		sent = sent + "".join(["!" for h in range(randint(1,9))])

	if i == max_iterations-1:
		output.append("alias b" + str(i) + " \"say " + sent + ";alias bindsnack b0\"")	
	else:
		output.append("alias b" + str(i) + " \"say " + sent + ";alias bindsnack b"+ str(i+1) + "\"")

output.append("\n\n")


target = open(file_path, 'w')
target.write(default + "\n".join(output))
target.close()
#
#	bind f1 bindknapp
#	alias bindknapp a1
#
#	alias a1 "buy bs;alias bindknapp a2"
#	alias a2 "buy bs;alias bindknapp a3"
#
#	alias a420 "buy bs; alias bindknapp a1"
#

# C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg