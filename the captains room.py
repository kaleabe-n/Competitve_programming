# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = [int(x) for x in input().split()]
count = {}
for i in rooms:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
print([x for x in count.keys() if count[x] == 1][0])
