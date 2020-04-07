# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:02:39 2020

@author: HUY-LAP
"""
# Lam viec voi mang 2 chieu
import random

m = int(input("Nhap m = "))
n = int(input("Nhap n = "))

a = []

for i in range(0, m):
    a.append([])
    for j in range(0, n):
        a[i].append(random.randint(1,9))

print("Day so vua nhap la: ")
for i in range(0, m):
    for j in range(0, n):
        print("%2d " % a[i][j], end='')
    print()

"""
# Cách 2:
print("Day so vua nhap la: ")
print(a)
"""