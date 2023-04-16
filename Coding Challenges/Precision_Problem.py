#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    length = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for item in arr:
        #print(item)
        if item > 0:
            #print("Ohhkay")
            pos += 1
        elif item < 0:
            #print("noooo")
            neg += 1
        else:
            #print("I guess am a zero")
            zero += 1

    per_pos = pos / length
    per_pos = "{0:.6f}".format(per_pos)
    print(per_pos)
    
    neg_pos = neg / length
    neg_pos = "{0:.6f}".format(neg_pos)
    print(neg_pos)
    
    zero_pos = zero / length
    zero_pos = "{0:.6f}".format(zero_pos)
    print(zero_pos)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
