testCount = int(input())
for _ in range(testCount):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    removed = 0
    for i in range(1,n):
        if arr[i] == arr[i-1] + 1 or arr[i] == arr[i-1]:
            removed += 1
    if removed + 1 == n:
        print("YES")
    else:
        print("NO")
