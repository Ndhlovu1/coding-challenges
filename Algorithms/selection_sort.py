"""
1. Take an Array item and iterate from left to right and swap this value with the lowest value found to the right of this item
2. Repeat this process with every single value in the array until it is sorted
"""

#Considering the Space and the Time Complexity of this Algorithm
"""
---------------------------------
SPACE COMPLEXIT = O(1) Auxillary
---------------------------------
TIME COMPLEXITY :
    WORST CASE      = 0(n**2)
    AVERAGE CASE    = 0(n**2)
    BEST CASE       = 0(n**2)
---------------------------------

"""

# STEPS TO CREATE A SELECTION SORT ALGORITHM(ST-A)
"""
1. Find the SMALLEST Value and Swap it with the first place of the array
2. FInd the second SMALLEST Value and Swap it with second place in the array
3. Repeat the Above steps until all items are changed and ordered from SMALLEST TO LARGEST
"""

# TIME COMPLEXITY IS DETERMINED IN RELATION TO THE NUMBER OF TRANSACTIONS DONE. 
# GIVEN A LIST OF size n, THE COMPILER MUST SEARCH EACH ENTRY IN THE LIST TO IDENTIFY THE SMALLEST ITEM THEN SWAP TO INDEX 0.

# The Pseoudocode
"""
for (i = 0; i<n-1; i++)
int min_index = List[i]
    for (j = i +1; j < n; j++)
        if(List[j] < List[min_index])
            min_index = j
    swap(List[i], List[min_index])
"""

# THE PSEUDOCODE BREAKDOWN
"""
LINE 31 -> Informs the program it must search n-1 times
LINE 32 -> Sets a temporary minimum value List[i]
LINE 33 -> An inner loop iterating through n-1 times
LINE 34 -> Verifies if the value found in position List[j] is smaller than the current min_index if true
LINE 35 -> The current position of this element is recorded
LINE 36 -> The value found to be the lowest is swapped with the position i
I will be incremented and the loop will repeat once more

"""

# PSEUDOCODE TIME AND SPACE COMPLEXITY BREAKDOWN
"""
---------------------------------
SPACE COMPLEXITY OF THIS APPROACH - ONLY AN IN-ARRAY SWAP IS OCCURING HENCE NO DUPLICATION OF DATA IS BEING MADE
                                    THERE ARE 3 TEMPORARY VARIABLES BUT THEY DON'T DEPEND ON THE LIST SIZE(minIndex, i and j)
                                    The SPACE COMPLEXITY DOESN'T INCREASE
                                    
---------------------------------
TIME COMPEXITY OF THIS APPROACH :
    1. WORST CASE - Given the list sorted in reverse order, how many checks are made?
                    The Inner and Outer Loops will have to run n times 
                    O(n**2)

    2. AVERAGE CASE -   Regardless of the order of the list, each item must be checked against avarage case
                        O(n**2)
                        
    3. BEST CASE -  Given a sorted list from smallest to largest how many comarisons must be made? It will still be the same 
                    the enitire double loops must be done twice
                    O(n**2) 

"""



