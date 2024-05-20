#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Function takes an integer of 5

def miniMaxSum(arr):
    # Write your code here
    i = 0
    total = sum(arr)
    mini = total
    maxi = 0
    while i < 5:
    	if (total - arr[i]) < mini:
    		mini = (total - arr[i])
    	if (total - arr[i]) > maxi:
    		maxi = (total - arr[i])
    	i += 1
    print (mini, maxi)


        
        
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
