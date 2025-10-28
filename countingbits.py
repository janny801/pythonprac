'''
problem; https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=dynamic-programming
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''

from typing import List


def countBits( n:int) -> List[int]: 
    #initialize values with 0 
    ans = [0] * (n+1)

    #iterate thu 
    #//2 divide by 2+ (%2) remainder 
        #for each value up to (and including) n 

    for curr in range(1, n+1):
        ans[curr] = ans[curr//2] + (curr%2)
    return ans

if __name__ == '__main__': 
    #main func 
    testinput1= 2
    testinput2 = 5

    print(countBits(testinput1)) 
    print(countBits(testinput2))
    

