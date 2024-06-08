'''
Valid Parentheses

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


def evaluate(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in bracket_map.values():  # if it's one of '(', '[', '{'
            stack.append(c)
        elif c in bracket_map:  # if it's one of ')', ']', '}'
            if not stack or bracket_map[c] != stack.pop():
                return False
        else:
            return False  # in case the string contains invalid characters

    return not stack


print(evaluate("{}"))
