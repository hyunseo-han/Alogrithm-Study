#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:37:41 2025

@author: hyunseo
"""

#20546_The Miraclce Trade
def bnp(money, stock, stock_price):
    for i in stock_price:
        stock += money // i
        money = money % i
        if(money == 0):
            break
    return money + stock * int(stock_price[13])
    

def timing(money, stock, stock_price):
    for i in range(3, 14):  # Started comparing 3 days ago
        # 3 consecutive days of gains → sell all
        if stock_price[i-3] < stock_price[i-2] < stock_price[i-1] < stock_price[i]:
            money += stock * stock_price[i]
            stock = 0
        # Down for 3 consecutive days → Buy as much as possible 
        elif stock_price[i-3] > stock_price[i-2] > stock_price[i-1] > stock_price[i]:
            stock += money // stock_price[i]
            money %= stock_price[i]
    return money + stock * stock_price[13]
 
    
    
money = int(input())
stock = 0
stock_price = list(map(int, input().split()))
    
print(bnp(money, stock, stock_price))
print(timing(money, stock, stock_price))


if(bnp(money, stock, stock_price) > timing(money, stock, stock_price)):
    print("BNP")
elif(bnp(money, stock, stock_price) < timing(money, stock, stock_price)):
    print("TIMING")
else:
    print("SAMESAME")
