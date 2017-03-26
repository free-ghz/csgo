# Random CS-GO buy bindings

* This is a script that makes you buy "random" items every time you press a button.
* It's a python script that overwrites your autoexec.cfg. (or another file)
* It generates two flavours of random buy binds: the cheap and the expensive.
* Both tries to give you a total loadout. Cheap gives you an smg or a gun, expensive gives you more shit.
* It also makes two keys for random talk in the chat which really annoys people :)
* It actually randomizes 420 aliases per key and cycles through them every time you press the key.
* Due to this it's good to run it once a day or so, or more often if you wish. On linux use cronjobs i guess, on windows use the task scheduler. That one scheduler is not that fun to work with but you'll get the hang of it. Important is that you write "python" as the program and [path to this script] as parameters. You don't have to run it as administrator for some reason even if it's in the program files folder.
* You WILL need to install python if you haven't already, i think any 2.7 is fine but just install the newest one (not 3.x)
* Don't for get to open the script up and change the path to the autoexec.cfg file! (Here you can output to some other name and exec it manually inside counter strike, if your autoexec is too precious to muck around with).

## When i think about it...

If you edit the number of things to randomize from 420 to say 1337 maybe you just need to run it once. When the buy commands cycle you'll have forgotten the previous ones? Maybe?
* No - it resets to alias one when you restart counter strike. lame!!!!!

## Homework for next week:
How many aliases can cs:go hold?
* We dont know
Does it keep which alias we're on when you restart?
* NO, it resets.

## Ok thats it folks

Have a good one. No warranty yadda yadda.