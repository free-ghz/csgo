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
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
max_iterations = 4200

# where to save the shit to, i like autoexec, you could choose whatever
file_path = "output.txt"






output = []




#
#	generera ~nice talk
#

for i in range(max_iterations):
	whichform = randint(0,4) # biased to algorithm C because its funnier
	if whichform == 0:
		sent = sentences_a.produce(True)
	elif whichform == 1:
		sent = sentences_b.produce(True)
	else:
		sent = sentences_c.produce(True)
	
	output.append(sent)

for i in range(max_iterations):
	whichform = randint(0,3)
	if whichform == 0:
		sent = sentences_a.produce(False)
	elif whichform == 1:
		sent = sentences_b.produce(False)
	else:
		sent = sentences_c.produce(False)
	
	output.append(sent)
	


target = open(file_path, 'w')
target.write("\n".join(output))
target.close()

# C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg