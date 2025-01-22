#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:42:12 2025

@author: hyunseo
"""

# 1012 Organic cabbage
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True  # Handling visits to your current location 현재 위치 방문 처리
    
    # Directional vectors for up, down, left, and right movement 상하좌우 이동을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # Explore only places that have cabbages and have not been visited 배추가 있고 방문하지 않은 곳만 탐색
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

# Enter test case
tc = int(input())

for i in range(tc):
    n, m, num = map(int, input().split())  
    arr = [[0 for _ in range(m)] for _ in range(n)] 
    visited = [[False for _ in range(m)] for _ in range(n)] 

   
    for j in range(num):
        x, y = map(int, input().split())
        arr[x][y] = 1

    
    worm_count = 0  
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1 and not visited[x][y]:  
                bfs(x, y)
                worm_count += 1  

    print(worm_count)
