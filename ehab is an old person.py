n = int(input())
arr = [int(x) for x in input().split()]
hasOdd = False
hasEven = False
for num in arr:
    if num%2 == 0:
        hasEven = True
    if num %2 == 1:
        hasOdd = True
    if hasEven and hasOdd:
        break

if hasEven and hasOdd:
    arr.sort()
print(*arr)
