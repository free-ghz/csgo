#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from random import randint
from random import uniform
from random import choice
from pprint import pprint
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

# config

# where to save the shit to, i like autoexec, you could choose whatever
file_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\autoexec.cfg"

# ["key", maxCashToBuyFor]
key1 = ["f5", 1200]
key2 = ["f6", 2500]
key3 = ["f7", 4444]
key4 = ["f8", 10000]

chanceOfNoArmor = 0.4

gunsPerKey = 100

default = """
// luki sa att jag skulle skriva denna här
// to do with networks
rate "687500"

//ok detta är bra binds
bind f1 "buy vest;buy mag7;buy hegrenade";buy deagle"
bind f2 "buy vest"
bind f3 "buy vest;buy ak47;buy defuser;buy vesthelm"
bind f4 "buy vest;buy defuser;buy vesthelm"

// lite cool stuff
r_drawtracers_firstperson 0

// raddar
cl_radar_always_centered "0"
cl_radar_scale "0.3"
cl_hud_radar_scale "1.15"
cl_radar_icon_scale_min "1"
cl_radar_rotate "1"

// viewmodel bob
cl_righthand "1"
viewmodel_offset_x "0"
viewmodel_offset_y "-2"
viewmodel_offset_z "-2"
viewmodel_fov "54"
cl_bobamt_lat "0.1"
cl_bobamt_vert "0.1"
cl_bobcycle "0.1"
cl_viewmodel_shift_left_amt "0.5"
cl_viewmodel_shift_right_amt "0.5"

//ok nu är resten generated
echo "---------------------"
"""

default += """
alias runon "+forward;alias midmouse runoff"
alias runoff "-forward;alias midmouse runon"
alias midmouse "runon"
bind mouse3 midmouse
"""
#
#	v3.0 (18/11 17)
#		* rewrite from sratch
#		* no longer talk binds bc its not fun anymore
#		* 
#	v2.4 (29/3 17)
#		* name suggestions
#		* bugfix but forgot what
#		* middle mouse is run now
#	v2.3 (26/3 17)
#		* fixed bug "sg008" --> "ssg08"
#		* made it echo generation time so you know if it's fresh
#		* removed the mysql thingy, fuck 40 sec generation time
#		* f7 = more trashy than f8
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


output = [default]

nades =  ["hegrenade","flashbang","smokegrenade","decoy","molotov","incgrenade"]

slot2 = [("p250", 300), 
	("elite", 400), 
	("deagle", 700), 
	("tec9", 500)]
slot1 = [("nova", 1200), 
	("xm1014", 2000), 
	("mag7/sawedoff", 1800),
	("m249", 5200),
	("negev", 2000),
	("mp9/mac10", 1250),
	("bizon", 1400),
	("ump45", 1200),
	("p90", 2350),
	("famas/galilar", 2250),
	("ak47/m4a1/m4a1_silencer", 2700),
	("sg556/aug", 3300),
	("ssg08", 1700),
	("awp", 4750),
	("scar20/g3sg1", 5000)
]
slot3 = [
	("flashbang", 200),
	("decoy", 50),
	("smokegrenade", 300),
	("hegrenade", 300),
	("incgrenade/molotov", 600)
]

key1.append("msa")
key2.append("msb")
key3.append("msc")
key4.append("msd")
variants = [key1, key2, key3, key4]

def buygun(guns, cash):
		# 3.1  selection
		possibleguns = []
		for gun in guns:
			if gun[1] <= cash:
				possibleguns.append(gun)
		if len(possibleguns) > 0:				
			return choice(possibleguns)
		else:
			return None
		# 3.2 purchasing

for variant in variants:
	output.append("bind " + variant[0] + " " + variant[2] + "pointer")
	output.append("alias " + variant[2] + "pointer " + variant[2] + "0")
	for rotation in xrange(gunsPerKey):
		# 1. setup
		string = "alias " + variant[2] + str(rotation) + " \""
		cash = variant[1]
		# 2. protection
		if (uniform(0,1) > chanceOfNoArmor):
			string += "buy vest;"
			cash -= 600
		# buy slot 1
		gun = buygun(slot1, cash)
		if gun != None:
			cash -= gun[1]
			if ("/" in gun[0]):
				t = gun[0].split("/")
				for g in t:
					string += "buy " + g + ";"
			else:
				string += "buy " + gun[0] + ";"
		# buy slot 2
		gun = buygun(slot2, cash)
		if gun != None:
			cash -= gun[1]
			if ("/" in gun[0]):
				t = gun[0].split("/")
				for g in t:
					string += "buy " + g + ";"
			else:
				string += "buy " + gun[0] + ";"

		# buy grenades?
		for f in xrange(3):
			temp = slot3[:]
			gun = buygun(temp, cash)
			if gun != None:
				temp.remove(gun)
				cash -= gun[1]
				if ("/" in gun[0]):
					t = gun[0].split("/")
					for g in t:
						string += "buy " + g + ";"
				else:
					string += "buy " + gun[0] + ";"

		# finish up
		if rotation == gunsPerKey-1:
			t = 0
		else:
			t = rotation+1
		string += "alias " + variant[2] + "pointer " + str(t) + "\""
		output.append(string)

whatsay = choice(["it's time to frag", "welcome to die", "get rekt, friends", "now we play cs go", "its time to git gud", "i buy deagle every time"])
output.append('say "' + whatsay + '"')

target = open(file_path, 'w')
target.write(default + "\n".join(output))
target.close()