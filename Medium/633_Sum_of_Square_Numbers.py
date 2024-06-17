'''
633. Sum of Square Numbers

Given a non-negative integer c, 
decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math

        if c < 0:
            return False

        for i in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - i * i)
            if b == int(b):
                return True
        return False


# Example usage
solution = Solution()
print(solution.judgeSquareSum(5))  # Output: True
print(solution.judgeSquareSum(3))  # Output: False
print(solution.judgeSquareSum(4))  # Output: True
print(solution.judgeSquareSum(1))  # Output: True
print(solution.judgeSquareSum(0))  # Output: True
