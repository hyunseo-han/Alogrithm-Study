#!/usr/birow/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:07:52 2025

@author: hyunseo
"""

row, column = map(int, input().split()) #N: 행(row)의 수, column: 열(column)의 수. 
a = [list(input()) for _ in range(row)] #체스판의 색깔 정보를 입력받아 2차원 리스트 a에 저장한다.
min_cnt = 32 #32가 최대

for i in range(row-7): #8X8 체스판을 선택
    for j in range(column-7):
        cnt = 0 #새로 칠해야하는 칸의 수
        for k in range(i, i+8): #선택한 8x8 체스판 탐색
            for l in range(j, j+8):
                # 인덱스 합이 짝수인 B색 칸 개수 + 인덱스 합이 홀수인 W색 칸 개수
                if ((k + l) % 2 == 0 and a[k][l] == 'B') or ((k + l) % 2 == 1 and a[k][l] == 'W'):
                    cnt += 1 #새로 칠해야 하는 수 증가
        cnt = min(cnt, 64-cnt) 
        if cnt < min_cnt: #현재까지 계산한 cnt와 기존의 min_cnt를 비교
            min_cnt = cnt
print(min_cnt)