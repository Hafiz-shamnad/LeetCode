'''
502. IPO

Suppose LeetCode will start its IPO soon. 
In order to sell a good price of its shares to Venture Capital, 
LeetCode would like to work on some projects to increase its capital before the IPO. 
Since it has limited resources, it can only finish at most k distinct projects before the IPO.
Help LeetCode design the best way to maximize its total capital 
after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] 
and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain 
its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize 
your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project 
indexed 2 to get the maximum capital.u
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6

'''
import heapq

def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    projects = [(capital[i], profits[i]) for i in range(n)]
    projects.sort()  # Sort projects based on capital requirements

    max_heap = []  # Max heap to store potential profits of projects we can afford
    idx = 0
    count = 0
    
    while k > 0:
        # Push all projects that we can afford into max heap
        while idx < n and projects[idx][0] <= w:
            heapq.heappush(max_heap, -projects[idx][1])  # Push negative profit to simulate max heap
            idx += 1
        
        if max_heap:
            # Select the project with maximum profit that we can afford
            max_profit = -heapq.heappop(max_heap)
            w += max_profit  # Update available capital
            count += 1
        else:
            break
        
        k -= 1

    return w

# Example usage:
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(findMaximizedCapital(k, w, profits, capital))  # Output: 4

k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]
print(findMaximizedCapital(k, w, profits, capital))  # Output: 6
