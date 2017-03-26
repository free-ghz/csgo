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
thing =  ["defuser","vesthelm"]
everything = [pistol, smg, nades, thing]

default = "// luki sa att jag skulle skriva denna här\n// to do with networks\nrate \"687500\"\n//ok detta är bra binds\n"
default += "bind f1 \"buy tec9\"\nbind f2 \"buy vest;buy defuser;buy vesthelm\"\nbind f3 \"buy vest;buy ak47;buy defuser;buy vesthelm\"\nbind f4 \"buy vest;buy mp7\"\n//ok nu är resten generated\n"

csgo_words = [("HACK", 1), ("hack", 1), ("stop cheating", 1), ("cheat", 1), ("toggle", 1), ("VAC", 1), ("vacation", 1), ("fuck", 3),("heck", 2),("fucking", 4),("ass", 3),("damg", 2),("shjit", 2),("bullshit",  1),("dont step", 1),("shut up", 1),("youre good", 1),("nice one", 2),("well jobbed", 1),("thanks", 1),("bro", 3),("dude", 3),("man", 2),("wtf", 5),("omg", 2),("lmao", 2),("godforsaken", 1),("of shit", 3),("piss", 3),("win the game", 2),("winn the shit", 1),("clan", 1),("worst", 1),("leave", 1),("pls", 2),("plz", 1),("wurst", 1),("sausage", 1),("cry", 1),("p12", 1),("12yo", 1),("russian", 2),("poland", 1),("buy ak all", 1),("buy kev", 1),("buy awp all", 1),("buy negev", 1),("no", 4),("yes", 1),("rush", 2),("all", 2),("nice skin", 1),("suck", 1),("lose", 1),("get rekt", 1),("git gud", 1),("best round", 1),("gg", 3),("bg", 1),("noob", 4),("knob", 1),("n00b", 1),("newb", 1),("youll", 2),("yall better", 2),("its", 2),("were", 1),("im gonna", 1),("you" , 2),("SUKA", 1),("blyat", 1),("idiot", 2),("master", 1),("player", 1),("ace", 2),("bomb a", 1),("bomb b", 1),("plant", 2),("dont plant", 2),("afk", 2),("defuse", 2),("dont defuse", 3),("15-15", 1),("16-15", 2),("16-0", 1),("good play", 3),("nice job", 3),("hopy shit yes", 3),("well done", 3),("well", 3),("ilu xo", 1),("haha", 2),("well fucked", 1),("tu madre", 1),("1v1", 2),("shrek", 2),("rekt", 2),("nice man", 2),("kick", 2),("clutch", 2),("awp mid", 1),("awp long", 1),("awp", 2),("eco", 2),("knife round", 1),("fuck yes", 2)]

csgo_good = [("fuck", 3), ("heck", 2), ("fucking", 5), ("ass", 2), ("thanks", 2), ("bro", 3), ("dude", 2), ("man", 2), ("wtf", 4), ("omg", 3), ("lmao", 2), ("pls", 2), ("no", 3), ("yes", 4), ("suck", 2), ("lose", 2), ("all", 2), ("rush", 2), ("gg", 4), ("bg", 2), ("noob", 2), ("its", 2), ("were", 2), ("idiot", 4), ("ace", 4), ("dont plant", 2), ("afk", 2), ("defuse", 2), ("good play", 2), ("nice job", 2), ("good", 4), ("nice", 4), ("i", 2), ("haha", 2), ("rekt", 3), ("smoke", 2), ("spray", 2), ("stop", 2), ("a", 2), ("you", 2), ("dont", 3), ("hmm", 3), ("hmmmm", 3), ("why", 2)];
csgo_hmmm = [("HACK", 2),("hack", 2),("stop cheating", 2),("cheat", 2),("toggle", 1),("VAC", 1),("vacation", 1),("damg", 2),("shjit", 1),("bullshit", 2),("dont step", 3),("shut up", 2),("youre good", 1),("nice one", 4),("well jobbed", 1),("godforsaken", 1),("of shit", 2),("piss", 3),("win thgame", 2),("winn the shit", 1),("clan", 2),("worst", 2),("leave", 3),("plz", 2),("wurst", 2),("sausage", 1),("cry", 1),("p12", 3),("12yo", 1),("russian", 2),("poland", 1),("buy ak all", 1),("buy kev", 1),("buy awp all", 1),("buy negev", 1),("nice skin", 1),("get rekt", 2),("git gud"),("best round", 2),("knob", 2),("n00b", 2),("newb", 2),("youll", 2),("yall better", 3),("im gonna", 2),("you", 3),("blyat", 2),("master", 1),("player", 1),("bomb a", 1),("bomb b", 1),("plant", 2),("dont defuse", 3),("15-15", 1),("16-15", 1),("16-0", 1),("holy shit", 1),("well done", 1), 
("well", 3),("ilu xo", 1),("well fucked", 1),("tu madre", 1),("1v1", 2),("shrek", 1),("herrmoroids", 1),("cripple", 1),("nice man", 2),("kick", 3),("clutch", 1),("awp mid", 1),("awp long", 1),("awp", 3),("eco", 3),("knife round", 1),("fuck yes", 3),("leftist", 2),("all i know",),("subversive", 1),("stop downloading", 1),("plastic", 1),("ninja", 1),("regressive", 1),("micro", 1),("macro", 1),("aim", 3),("AIM", 2),("spray control", 3),("cs:good", 2),("nvidia", 1),("kek", 3),("please", 3),("donald", 1),("cracker", 1),("homo", 2),("no", 5),("no homo", 1),("better", 1),("vodka", 1),("keylogger", 1),("KGB", 1),("NSA", 1),("CIA", 1),("ukraine", 1),("yea", 2),("are", 2),("will", 1),("national guard of ukraine", 1),("maga", 1),("great again", 1),("make", 1),("do", 1),("dont", 1),("pepe", 1),("meme", 1)];
csgo_words = csgo_good + csgo_good + csgo_words;
unfurled = []

output = []

#
#	generera vapenbinds
#

default += "bind f5 bindknapp\nalias bindknapp a0\n"

for i in range(max_iterations):
	clean = [True, True, True, True]
	sent = "alias a" + str(i) + " \"buy vest;buy "
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
	if randint(0,4) == 1:
		for x in range(randint(1,2)):
			where = randint(0,len(sent))
			sent = sent[:where] + " " + sent[where:]
	# kanske ett komma
	if randint(0,8) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + "," + sent[where:]
	# kanske ett apostrophy
	if randint(0,9) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + "'" + sent[where:]
	if randint(0,2) == 1:
		where = randint(0,len(sent))
		sent = sent[:where] + choice(string.letters.lower()) + sent[where:]
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



