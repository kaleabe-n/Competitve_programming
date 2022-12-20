# Enter your code here. Read input from STDIN. Print output to STDOUT
ml,nl = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a = set(a)
b = set(b)
happiness = 0
for i in arr:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1
print(happiness)
