# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split()
setCount = int(input())
sets = []
for _ in range(setCount):
    newSet = input().split()
    newSet = set(newSet)
    sets.append(newSet)
for item in sets:
    if not(item.issubset(a) or len(a)<=len(item)):
        print("False")
        break
else:
    print("True")  
