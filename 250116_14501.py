#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:36:27 2025

@author: hyunseo
"""

#14501 Resign

def benefit ():
    return 0
    
    
n = int(input())

data = []
for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))

# check
print(data)

print(benefit(data))