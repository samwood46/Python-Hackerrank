
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    PATHCOUNTER = 0
    splited = path
    VALLEYS = 0
    inValley = False
    i = 0
    while i < steps:
    	if splited[i] == 'D':
    		PATHCOUNTER -= 1
    		if (PATHCOUNTER == -1 and inValley == False):
    			#VALLEYS +=1

    			inValley = True


    	elif splited[i] == 'U':
    		PATHCOUNTER += 1
    		if (PATHCOUNTER == 0 and inValley == True):
    			VALLEYS +=1
    			inValley = False
    	i +=1

    return VALLEYS

if __name__ == '__main__':
    fptr = sys.stdout

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()