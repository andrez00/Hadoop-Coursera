#!/usr/bin/env python
import sys


#----
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#[Source code] https://github.com/kiichi/CourseraBigData/blob/master/map_reduce_join_python/join2_reducer.py
#----
last_key      = None              #initialize these variables
running_total = 0
abc_found = False
key_out = None

#read lines, and split lines into key & value
for line in sys.stdin:
	line = line.strip() #strip out carriage return
	key_value  = line.split('\t') #split line, into key and value, returns a list
	value = 0
	if key_value[1].isdigit():
		value = int(key_value[1])

	if key_value[0] == last_key: #if a key has changed (and it's not the first input)
		running_total += value #otherwise keep a running total of viewer counts
	else:
		if last_key and abc_found: # then check if ABC had been found and print out key and running total
			print("%s\t%d"%(key_out,running_total)) 
			abc_found = False
			running_total = value
if key_value[1] == 'ABC':  # if value is ABC then set some variable to mark that ABC was found (like abc_found = True)
		key_out = key_value[0]  
		abc_found = True
		last_key  = key_value[0]