#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:40:21 2025

@author: hyunseo
"""

n = int(input())

# 가장 작은 생성자를 저장할 변수 (초기값은 0으로 설정)
min_creator = 0

# 1부터 N까지 반복하여 생성자를 찾음
for i in range(1, n + 1):
    # i의 분해합 계산
    digit_sum = sum(int(digit) for digit in str(i))
    decomposition_sum = i + digit_sum
    
    # 분해합이 n과 같다면 i는 생성자
    if decomposition_sum == n:
        min_creator = i
        break  # 가장 작은 생성자를 찾았으므로 종료

print(min_creator)
