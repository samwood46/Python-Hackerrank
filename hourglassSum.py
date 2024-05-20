#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
	j = 0
	#i = 0#####
	hgs = []
	nums = [0,1,2,3,6,7,8,9,12,13,14,15,18,19,20,21]
	while j < len(nums):
		jg = 0
		i = nums[j]
		hg = arr[i] +arr[i+1] + arr[i+2] + arr[i+7] + arr[i+12] + arr[i+13] +arr[i+14]
		hgs.append(hg)
		j += 1
	big_hg = 0
	i = 0
	while i < len(hgs)-1:
		if hgs[i] <hgs[i+1]:
			big_hg = hgs[i+1]
		else:
			big_hg = big_hg
		i += 1

	return big_hg