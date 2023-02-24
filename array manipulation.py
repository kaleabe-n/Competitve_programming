def arrayManipulation(n, queries):
    # Write your code here
    maxx = 0
    prefix = [0]*n
    for left,right,num in queries:
        prefix[left-1]+=num
        if right<n:
            prefix[right]-=num
    pre = 0
    for num in prefix:
        pre+=num
        maxx = max(maxx,pre)
    return maxx
