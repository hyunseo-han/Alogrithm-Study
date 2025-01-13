#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:11:24 2025

@author: hyunseo
"""

def find_squre(s):
    for i in range(row-s+1): # 행
        for j in range(column-s+1): # 열
            if num[i][j] == num[i][j+s-1] == num[i+s-1][j] == num[i+s-1][j+s-1]:
                return True

    return False


row, column = map(int, input().split())
num = [list(map(int, list(input()))) for _ in range(row)]
#string -> integer character by character to create a list
#문자열을 정수로 바꿔 리스트 만들
기

size = min(row,column) #Max size of square 정사각형의 최대 크기

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k):
        print(k*k) #Square K to find area 제ㅔ곱해서 넓이 구하기
        break
    
    