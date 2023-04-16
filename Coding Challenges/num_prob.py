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
#

def miniMaxSum(arr):
    # Write your code here
    #arr = [5,5, 5, 5, 5]
    #print("Max",max(arr))
    
    max_value = max(arr)
    min_val = min(arr)
    
    min_sum = 0
    max_sum = 0
    
    min_same_sum = 0
    max_same_sum = 0
    
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    e = arr[4]
    
    for item in arr:
        if item != max_value:
            #print(item)
            max_sum += item 
            #print("Calling from 1st")
    
        if (item != min_val) :
            min_sum += item
            #print("Calling from 2rd")
            
        if (max_value == min_val):
            max_same_sum += item
            min_same_sum += item
            
            if(item == e):
                max_sum = max_same_sum - item
                min_sum = min_same_sum - item
            
        #elif item == a and item == b and item == c and item == d and item == e:
         #   max_sum += item
          #  min_sum += item
            
    #print("Max :",max_sum)
    #print("Min :",min_sum)
    print(max_sum,min_sum)
            
            
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
