#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
def median(arr):
    arr.sort()
    l = len(arr)
    index = l // 2
    for i in range(l):
        # find if length is % 2
        if (l % 2 != 0): # odd
            
            median = arr[index]
        else:
            index2 = (l //2) - 1
            #print ('index2: ' , index2)
            median = (arr[index] + arr[index2]) / 2
    return median



def runningMedian(a):
    # Write your code here
    result = []
    a2 = []
    for i in range(len(a)):
        a2.append(a[i])
        result.append(median(a2))
    return result



if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
