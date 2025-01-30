#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:43:49 2025

@author: hyunseo
"""

# 1463 Make it 1
def make_one(n):
    dp = [0] * (n + 1)  # Initialize the DP table
    
    for i in range(2, n + 1):
        # The default operation is subtracting 1
        dp[i] = dp[i - 1] + 1  
        
        # If divisible by 2, compare with the result of dividing by 2
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # If divisible by 3, compare with the result of dividing by 3
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]  # Return the minimum number of operations to make n equal to 1

n = int(input())  # Read input
print(make_one(n))  # Print the minimum number of operations
