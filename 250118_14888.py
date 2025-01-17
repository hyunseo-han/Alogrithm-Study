#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:00:12 2025

@author: hyunseo
"""

#14888 Insert operators
import sys

# 최댓값과 최솟값 초기화
max_result = -sys.maxsize
min_result = sys.maxsize

# 연산 수행 함수
def calculate(a, b, operator):
    if operator == 0:  # 덧셈
        return a + b
    elif operator == 1:  # 뺄셈
        return a - b
    elif operator == 2:  # 곱셈
        return a * b
    elif operator == 3:  # 나눗셈
        # 음수 나눗셈 처리 (C++ 기준)
        if a < 0:
            return -(-a // b)
        else:
            return a // b

# DFS 함수
def dfs(index, current_result, operators):
    global max_result, min_result

    # 모든 수를 사용했을 때 결과 갱신
    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 남아있는 연산자 사용
    for i in range(4):  # 0: +, 1: -, 2: *, 3: /
        if operators[i] > 0:
            # 연산자 사용
            operators[i] -= 1
            next_result = calculate(current_result, numbers[index], i)
            dfs(index + 1, next_result, operators)
            operators[i] += 1  # 백트래킹 (연산자 복구)

# 입력 받기
n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트
operators = list(map(int, input().split()))  # [+, -, *, /] 연산자 개수

# DFS 시작
dfs(1, numbers[0], operators)

# 결과 출력
print(max_result)
print(min_result)
