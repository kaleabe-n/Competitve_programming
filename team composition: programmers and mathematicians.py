t = int(input())
for _ in range(t):
    a,b = [int(x) for x in input().split()]
    l = 0
    r = (a+b)//4
    total = a+b
    while l<=r:
        mid = (l+r)//2
        if min(a,b)>=mid:
            l = mid+1
        else:
            r = mid-1
            
    print(r)
        
