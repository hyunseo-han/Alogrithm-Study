#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:27:23 2025

@author: hyunseo
"""
tri = [i * (i + 1) // 2 for i in range(1, 46)]  # 45번째 삼각수 == 1035
eur = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            num = i + j + k
            if num <= 1000:
                eur[num] = 1 # 세 숫자의 조합으로 만들어지는 수

t = int(input())
for _ in range(t):
    print(eur[int(input())])
