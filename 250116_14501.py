#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:36:27 2025

@author: hyunseo
"""

#14501 Resign 퇴사

def benefit (data):
    length = len(data)
    dp = [0] * (length + 2) # Create an array of size n+2 to consider up to n+1 
    
    for i in range(length, 0, -1): # Calculate max profit in reverse order starting from the last day
        t, p = data[i - 1] # Duration and revenue for consultation i
    
        # Check consultation availability and update DP
        if (i + t - 1) <= length:
            dp[i] = max(p + dp[i + t], dp[i + 1]) #
        else:
            dp[i] = dp[i + 1]
        
    print(dp)
    return dp[1] # DP[1] stores the maximum profit you could have earned if you started on day 1
    
    
n = int(input())

data = [] #tuple list
for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))

print(benefit(data)) 