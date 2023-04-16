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
    item = s
    fs_two = item[:2] 
    if item[-2:] == "PM" and int(fs_two) > 12:
        #print(item," ATTEMPT --",item[0:8])
        desired_values = item[0:8]
        
        last_position = item[-2:]
        #print("LAST TWO", last_position)
        first_position = item[:2]
        
        #print("FIRST TWO", first_position)
        add_first_pos = int(first_position)
        #print("ADDED VALUES", add_first_pos)
        
        final_time_val = str(add_first_pos)
        changed_val = desired_values.replace(first_position,final_time_val)
        item = changed_val
        print("REPLACED AND ADDED THE VALUES --- 01", item)
        
    
    elif item[-2:] == "PM" and int(fs_two) != 12:
        #print(item," ATTEMPT --",item[0:8])
        desired_values = item[0:8]
        
        last_position = item[-2:]
        #print("LAST TWO", last_position)
        first_position = item[:2]
        
        #print("FIRST TWO", first_position)
        add_first_pos = int(first_position) + 12
        #print("ADDED VALUES", add_first_pos)
        
        final_time_val = str(add_first_pos)
        changed_val = desired_values.replace(first_position,final_time_val)
        item = changed_val
        print("REPLACED AND ADDED THE VALUES --- 02", item)
            
        
        
    elif item[-2:] == "AM" and item[:2] == "12":
        
        desired_values = item[0:8]
        print(desired_values)
        last_position = item[-2:]
        
        first_position = item[:2]
        
        time_num = int(first_position) 
        #print(time_num)
        subd = 12 - time_num
        
        final_sbd = str(subd)
        
        changed_val = desired_values.replace(first_position, "00")
        item = changed_val 
        #print(item)
        print("REPLACED AND ADDED THE VALUES --- 03", item)
        
        
        
    elif item[-2:] == "AM":
        desired_values = item[0:8] 
        item = desired_values
        print(item,"I am Values")
        
        
        
        
        
    #Ensure that the code runs for the 00 and for the 12PM Notation
    elif item[-2:] == "AM" and item[2:] == "12":
        desired_values = item[0:8]
        f_n = item[2:].replace(item[2:], "00")
        item = f_n
        print(item,"I am Values")
        
        
        
        
    #Ensure that the code runs for the 00 and for the 12PM Notation
    elif item[-2:] == "PM" and int(fs_two) == 12:
        
        desird_values = item[0:8]
        fn = item[-2:].replace(item[2:], "Boom")       
        print(fn, "Ohoak")
        item = desird_values
        
              
    
    return item 
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
