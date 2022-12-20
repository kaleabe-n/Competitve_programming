# Enter your code here. Read input from STDIN. Print output to STDOUT
testCases = int(input())
for i in range(testCases):
    boxCount = int(input())
    blockes = [int(x) for x in input().split()]
    i = 0
    j = len(blockes)-1
    pileTop = float('inf')
    while i<=j:
        if blockes[i]<=pileTop and blockes[j]<=pileTop:
            if blockes[i]>=blockes[j]:
                pileTop = blockes[i]
                i+=1
            else:
                pileTop = blockes[j]
                j-=1
        else:
            print("No")
            break
    else:
        print("Yes")   
