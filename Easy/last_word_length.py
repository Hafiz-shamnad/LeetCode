'''
Length of Last Word

Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal 
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''
# import string

s = "a"
# count = 0

# for i in range(len(s)-1 , -1 , -1):
#     if s[i] == ' ':
#         if count > 0:
#             break     
#     else:
#         for letter in string.ascii_letters:
#             if s[i] == letter:
#                 print(letter, end=" ")
#                 count += 1
#                 break
        

# print(count)

words = s.split()
print(len(words[len(words) - 1]))