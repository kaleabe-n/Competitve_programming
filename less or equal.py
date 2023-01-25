    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    num = arr[k-1]
    if k == 0:
        if arr[0] - 1>0:
            print(arr[0] - 1)
        else:
            print(-1)
    elif k<n and num == arr[k]:
        print(-1)
    else:
        print(num)
