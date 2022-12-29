import collections


testCount = int(input())
value = {}
value["S"] = 0
value["M"] = 1
value["L"] = 2
for i in range(testCount):
    n,c = [int(x) for x in input().split()]
    planetOrbits = input().split()
    count = collections.Counter(planetOrbits)
    ans = 0
    for num in count.values():
        if num >= c:
            ans+=c
        else:
            ans+=num
    print(ans)
    
