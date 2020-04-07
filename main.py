# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:05:06 2020

@author: HUY-LAP
"""
import random

card = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
arr = []
state = []

def create_table(row, col):
    ''' create data matrix '''
    a = []
    for i in range(0, row):
        a.append([])
        state.append([])
        nlist = random.sample(range(col), col)
        # print("|", end="")
        for j in range(0, col):
            a[i].append(card[nlist[j]])
            state[i].append(0)
    return a


def print_table(a, row, col):
    ''' print result matrix choose '''
    for i in range(0, int(rows)):
        for j in range(0, int(cols)):
            if state[i][j] == 0:
                print("%s\t" % a[i][j], end='')
            else:
                print("X\t", end='')
        print()

def print_choose(a, nrow, ncol, mrow, mcol):
    ''' print result matrix choose '''
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            if (i == nrow and j == ncol) or (i == mrow and j == mcol):
                print("%s\t" % a[i][j], end='')
            else:
                print("O\t", end='')
        print()

def print_rs(a):
    ''' print result matrix choose '''
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            if a[i][j] == 0:
                print("O\t", end='')
            else:
                print("X\t", end='')
        print()

# inp = input("Input number of row, col: ")
# rows, cols = inp.split(" ")
rows, cols = 4, 5
# rows = int(input("Input number of row: "))
# cols = int(input("Input number of col: "))

dt = create_table(int(rows), int(cols))
point = 0
print_table(dt, rows, cols)
while point < 8:
    # print_table(dt, int(rows), int(cols))
    print("============= Player =============")
    print_rs(state)
    print("==================================")
    inp = input("Input choose [1] (row, col): ")
    inp2 = input("Input choose [2] (row, col): ")
    print("==================================")
    nrow, ncol = inp.split(" ")
    mrow, mcol = inp2.split(" ")
    print_choose(dt, int(nrow), int(ncol), int(mrow), int(mcol))
    print("==================================") 
    if dt[int(nrow)][int(ncol)] == dt[int(mrow)][int(mcol)]:
        point += 2
        state[int(nrow)][int(ncol)] = state[int(mrow)][int(mcol)] = 1
        print("Congratulation!!! %d point" % point)
    else:
        print("Sorry -_-")

# print_table(dt, int(rows), int(cols))
print("==================================") 
print("Win game!!!")
