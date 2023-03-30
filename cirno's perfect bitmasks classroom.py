t = int(input())
for i in range(t):
    x = int(input())
    ans = 0
    count = 0
    while True:
        if x & 1:
            ans += 2**count
            if x>>1 !=0:
                break
            if count > 0:
                ans+=1
            else:
                count+=1
                ans += 2
            break
                 
        count+=1
        x = x>>1
 
    
    print(ans)
