'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

from typing import List

class Solution: 
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        numsteps = len(cost)

        #base cases 
            # outside of constraints on leetcode 
            #written js incase 
        if numsteps ==0: 
            return 0 #no steps -> no cost 
        if numsteps == 1: 
            return cost[0] #1 step; must may that cost 


        prevmincost = cost[0] #holds dp[i-2]
        currmincost = cost[1] #holds dp[i-1]

        for stepindex in range(2, numsteps): 
            #compute dp[i] using two prev computed dp vals 
            stepcost = cost[stepindex] + min(prevmincost, currmincost)

            #shift window forward
            # dp[i-2] is now the old dp[i-1]
            #dp[i-1] is now dp[i]
            prevmincost = currmincost
            currmincost = stepcost

        #to reach the top u can come from last or second to last step 
        return min(prevmincost, currmincost)

if __name__ =='__main__': 
    solver = Solution()

    testinput1= [10,15,20]
    testinput2 = [1,100,1,1,1,100,1,1,100,1]

    #run solver
    print(f"{testinput1} --> {solver.minCostClimbingStairs(testinput1)}") #expected 15
    print(f"{testinput2} --> {solver.minCostClimbingStairs(testinput2)}") #expected 6
