#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:56:10 2025

@author: hyunseo
"""

# 2748 Fibo2
n = int(input())

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Use a loop to calculate the Fibonacci sequence up to the nth number
for _ in range(n):
    a, b = b, a + b  # Update a to the next Fibonacci number, and b to the next sum

# Output the nth Fibonacci number
print(a)
