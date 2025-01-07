#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:21:44 2025

@author: hyunseo
"""

#2309 Seven dwarf

from itertools import combinations


heights = []

for _ in range(9):
	heights.append(int(input()))
               
               
for combo in combinations(heights, 7):
    if sum(combo) == 100:
        # 합이 100이 되는 경우 오름차순으로 정렬 후 출력
        result = sorted(combo)
        for height in result:
            print(height)
        break 
