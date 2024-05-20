import math
import os
import random
import re
import sys
#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    res = 0
    i = 0
    while i < n-1:
        if i+2< n and c[i+2] == 0:
            i = i+2
            res += 1
        else:
            i = i+1
            res += 1
    return(res)

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()