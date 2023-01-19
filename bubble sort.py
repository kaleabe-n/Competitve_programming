#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    i=0
    counter = 0
    while(i<len(a)):
        if(i!=0 and a[i]<a[i-1]):
            a[i],a[i-1]=a[i-1],a[i]
            counter+=1
            i=i-1
        else:
            i=i+1
    print('Array is sorted in',counter,'swaps.')
    print("First Element:",a[0])
    print("Last Element:",a[-1])
            

        
    
# def countSwaps(a):
#     swaps = 0
#     for _ in range(len(a)):
#         swapped = False
#         for i in range(len(a)-1):
#             if a[i] > a[i+1]:
#                 a[i],a[i+1] = a[i+1],a[i]
#                 swaps += 1
#                 swapped = True
#         if not swapped:
#             break
    
#     print("Array is sorted in", swaps, "swaps.")
#     print("First Element:",a[0])
#     print("Last Element:",a[-1])
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

            


