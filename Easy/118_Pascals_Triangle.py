'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''
# input n
numRows = 5
arr=[]
for i in range(1, numRows+1):
    arr_ap =[]
    arr.append(arr_ap)
    for j in range(0, numRows-i+1):
        C = 1
        arr_ap.append(C)
        break
    for j in range(1, i+1):
        C = C * (i - j) // j
        if C != 0 :
            arr_ap.append(C)
print(arr)
