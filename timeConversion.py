#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    l = len(s)
    if ((s[l-2:]) == 'AM'):
    	hour = s[:2]
    	if hour == "12":
    		print("00" + s[2:-2])
    	else:
    		print (s[:-2])
    else:
    	hour = int(s[:2])
    	if (hour < 12):
    		hour = hour + 12
    	if hour == 12:
    		hour = 12
    	hourString = str(hour)
    	print (hourString + s[2:-2])
    	
    	

if __name__ == '__main__':
    fptr = sys.stdout	

    s = input()

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
