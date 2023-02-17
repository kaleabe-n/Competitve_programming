    n,m = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    p = 0
    ans = []
    for num in arr2:
        while p < n and arr1[p] < num:
            p+=1
        ans.append(p)
        
    print(*ans)
