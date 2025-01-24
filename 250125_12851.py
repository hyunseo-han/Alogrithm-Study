#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:19:38 2025

@author: hyunseo
"""

# 12851 Hide and seek2
from collections import deque

def bfs(n, k):
    max_pos = 100000
    visited = [-1] * (max_pos + 1)  # Time to reach each position (-1 means not visited)
    count = [0] * (max_pos + 1)  # Number of ways to reach each position

    # Start BFS with initial position
    queue = deque([(n, 0)])  # (current position, current time)
    visited[n] = 0  # Time to reach starting position is 0
    count[n] = 1  # There's only 1 way to start at the initial position

    while queue:
        current, time = queue.popleft()

        # Explore possible moves
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_pos:
                # If the position is not visited or visited at the same time
                if visited[next_pos] == -1 or visited[next_pos] == time + 1:
                    if visited[next_pos] == -1:  # First time visiting this position
                        queue.append((next_pos, time + 1))
                        visited[next_pos] = time + 1  # Update time to reach this position

                    # Add to the count of ways to reach this position
                    count[next_pos] += count[current]

    return visited[k], count[k]

# Input handling
n, k = map(int, input().split())
time, ways = bfs(n, k)
print(time)
print(ways)

