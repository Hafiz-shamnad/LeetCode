'''
Unique Number of Occurrences

Hint
Given an array of integers arr, return true if the number of 
occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

arr = [1,2]
occ = []
counted = set()
flag = 0

for i in arr:
    if i not in counted:
        occ.append(arr.count(i))
        counted.add(i)

for i in range(len(occ)):
    for j in range(len(occ)):
        if i != j and occ[i] == occ[j]:
            flag = 1

if(not flag):
    print("List contains all unique elements")
else:
    print("List contains does not contains all unique elements")