#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:57:57 2025

@author: hyunseo
"""

# 1697 Hide and seek
from collections import deque

def bfs(n, k):
    # Array to check visited positions (range: 0 to 100,000)
    max_pos = 100000
    visited = [-1] * (max_pos + 1)  # -1 means not visited
    queue = deque([n])  # Starting position
    visited[n] = 0  # Time at the starting position is 0

    while queue:
        current = queue.popleft()

        # If the target position is reached, return the time
        if current == k:
            return visited[current]

        # Explore possible next positions
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# Input handling
n, k = map(int, input().split())
print(bfs(n, k))
