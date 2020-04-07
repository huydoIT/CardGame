# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:05:06 2020

@author: HUY-LAP
"""
import random

card = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
a = []

def printTable(row, col):
    for i in range(0, row):
        a.append([])
        nlist = random.sample(range(col), col)
        # print("|", end="")
        for j in range(0, col):
            a[i].append(card[nlist[j]])
            # print(" %s |" % random.choice(card), end="")
            # print(" %s" % card[nlist[j]], end="")
            # print("\t|", end="")
        # print("")

inp = input("Input number of row, col: ")
rows, cols = inp.split(" ")
# rows = int(input("Input number of row: "))
# cols = int(input("Input number of col: "))
print("=== Result ===")
printTable(int(rows), int(cols))
for i in range(0, int(rows)):
    for j in range(0, int(cols)):
        print("%s\t" % a[i][j], end='')
    print()

print("==============")
