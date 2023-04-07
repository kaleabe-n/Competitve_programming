n = int(input())
sources = set(range(1,n+1))
sinks = set(range(1,n+1))
for i in range(n):
    row = input().split()
    for j,val in enumerate(row):
        if val == '1':
            if j+1 in sources:
                sources.remove(j+1)
            if i+1 in sinks:
                sinks.remove(i+1)
print(len(sources),end = " ")
print(*sorted(sources))
print(len(sinks),end = " ")
print(*sorted(sinks))
