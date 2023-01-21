#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# def insertionSort1(n, arr):
#     # Write your code here
#     num=arr[n-1]
#     i=n-2
#     while(i>=0):
#         if(arr[i+1]<arr[i]):
#             num=arr[i+1]
#             arr[i+1]=arr[i]
#             print(*arr)
#             arr[i]=num
#         else:
#             break
#         i-=1
#     print(*arr)

def insertionSort1(n, arr):
    i = n - 1
    while  i > 0 and arr[i] < arr[i-1]:
        temp = arr[i]
        arr[i] = arr[i-1]
        print(*arr)
        arr[i-1] = temp
        i-=1
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
