#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    # Write your code here
    #for i in range(len(queries)):
    count = []
    contacts = []
    for i in range(queries_rows):        
        # add names into the contacts list
        if (queries[i][0] == 'add' and queries[i][1] not in contacts):
            contacts.append(queries[i][1])
        #print ('contacts ', contacts)
        #find method 
        if (queries[i][0] == 'find'):
            counter = 0
            # go backthrough contacts
            for j in range(len(contacts)):
                if (queries[i][1] in contacts[j]):
                    counter += 1
            count.append(counter)
    return count








fptr = sys.stdout

queries_rows = int(input().strip())
#queries_rows = 4

#queries = [['add', 'hac'], ['add', 'hack'], ['add', 'hack'], ['add', 'hack']]
queries = []
for _ in range(queries_rows):
    queries.append(input().rstrip().split())

result = contacts(queries)

fptr.write('\n'.join(map(str, result)))
fptr.write('\n')

fptr.close()
