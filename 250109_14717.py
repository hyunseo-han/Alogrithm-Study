#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:31:20 2025

@author: hyunseo
"""

def solve():
    # 콘솔에서 두 정수 a, b 입력 받기
    
        a, b = map(int, input().split())

        cases = 9 * 17  # 가능한 총 조합의 수
        ans = 0  # 조건을 만족하는 조합의 개수를 저장할 변수

        if a == b:  # a와 b가 같을 경우
            ans = cases - (10 - a)  # 조건에 맞지 않는 조합 제외
        else:  # a와 b가 다를 경우
            mypoint = (a + b) % 10  # 목표 값 계산

            for i in range(1, 11):  # 1부터 10까지 반복
                for j in range(i + 1, 11):  # i보다 큰 숫자 j를 반복
                    if mypoint > (i + j) % 10:  # 목표 값보다 작은 경우
                        if i == a and j == b:  # i, j가 a와 b와 정확히 일치하면 제외
                            continue
                        elif i == a or j == a or i == b or j == b:  # i 또는 j가 a 또는 b와 일치하면 조합 수 2 증가
                            ans += 2
                        else:  # 그 외의 경우 조합 수 4 증가
                            ans += 4

        # 결과 출력 (소수 셋째 자리까지 출력)
        print("%.3f" % (ans / cases))
        
    

# 함수 호출
solve()
