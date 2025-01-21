#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:06:41 2025

@author: hyunseo
"""

#11724 Connected Components
import sys
sys.setrecursionlimit(1000) #Increased recursion limit (required by DFS)
input = sys.stdin.read

# DFS 함수 정의
def dfs(node):
    visited[node] = True  # 현재 정점을 방문 처리
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 이웃 정점이 방문되지 않았다면 재귀 호출
            dfs(neighbor)    
    
    
N, M = map(int, input().split()) # N: vertex(정점), M: edge(간선) 
graph = [[]for _ in range(N+1)] # Create adjacency list

for _ in range(M):
    u, v = map(int, input().split())  # Enter edge
    graph[u].append(v)  # Add bidirectional because it's undirected graph
    graph[v].append(u)
    
# Counting the number of connection elements
visited = [False] * (N + 1)  # 방문 여부 리스트
connected_components = 0

for node in range(1, N + 1):
    if not visited[node]:  # 방문하지 않은 정점에서 탐색 시작
        dfs(node)
        connected_components += 1  # 한 번의 탐색이 끝나면 연결 요소 1개 추가

print(connected_components)