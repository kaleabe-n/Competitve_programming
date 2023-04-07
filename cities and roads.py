n = int(input())
count = 0
for i in range(n):
    row = input().split()
    for j in range(i):
        if row[j] == '1':
            count+=1
            
print(count)
