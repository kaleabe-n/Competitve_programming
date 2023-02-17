    n,m = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    p1 = 0
    p2 = 0
    arr = []
    while p1<n or p2<m:
        if p1 >= n:
            arr.append(arr2[p2])
            p2+=1
        elif p2 >= m or arr1[p1] <= arr2[p2]:
            arr.append(arr1[p1])
            p1+=1
        elif arr1[p1] > arr2[p2]:
            arr.append(arr2[p2])
            p2+=1
    print(*arr)
