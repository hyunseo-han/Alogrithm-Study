#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:40:08 2025

@author: hyunseo
"""

#14889 start and link
from itertools import combinations
import math

# Functions to calculate a team's stats
def team_ability(team, array):
    ability = 0
    # Pick two people from your team and add their stats together
    for i, j in combinations(team, 2):
        ability += array[i][j] + array[j][i]
    return ability

# Function to find the minimum value of a stat difference
def ability(array):
    global n
    members = range(n)
    min_diff = math.inf  # initialize

    # Get one team as a combination and set the rest to another team
    for team_a in combinations(members, n // 2):
        team_b = [member for member in members if member not in team_a]

        # Calculate ability
        ability_a = team_ability(team_a, array)
        ability_b = team_ability(team_b, array)

        # Calculate stat diff
        diff = abs(ability_a - ability_b)

        # if diff == 0, end immediately
        if diff == 0:
            return 0

        # Update minimum
        min_diff = min(min_diff, diff)

    return min_diff


n = int(input())
array = []

for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)


print(ability(array))
