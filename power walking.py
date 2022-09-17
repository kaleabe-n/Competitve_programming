for i in range(int(input())):
    n = int(input())
    powers = [int(x) for x in input().split()]
    types = set(powers)
    for i in range(1,n+1):
        print(max(i,len(types)),end = " ")
    print("")
        
