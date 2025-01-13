#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:07:05 2025

@author: hyunseo
"""

#1547 ball
arr = [0, 1, 0, 0]
num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
    
print(arr.index(1))

'''
for j in range(len(arr)):
    if(arr[j] == 1):
        print(j)
        break
'''