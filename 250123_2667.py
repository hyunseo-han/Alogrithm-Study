#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:52:27 2025

@author: hyunseo
"""

# 2667 Numbering 
n = int(input())
arr = [list(map(int, input())) for _ in range(n)] # Enter the map
visited = [[False for _ in range(n)] for _ in range(n)] # Visited or not

# Up, down, left, right directional vextors 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    stack = [(x, y)] #stack
    count = 0 # The number of house in map
    
    while stack:
        cx, cy = stack.pop()
        if not visited[cx][cy]: # if you haven't visited
            visited[cx][cy] = True 
            count += 1
            
            # Navigating up, down, left, right neighbors
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                    stack.append((nx, ny))
    return count

# Save number and size
complex_sizes = []

# Navigating the map
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]: # Find a new complex
            complex_size = dfs(i, j) # DFS
            complex_sizes.append(complex_size)
            
complex_sizes.sort() 
print(len(complex_sizes))
for size in complex_sizes:
    print(size)