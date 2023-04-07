n = int(input())
for _ in range(n):
    row = input().split()
    neighbours = []
    for i,val in enumerate(row):
        if val == '1':
            neighbours.append(i+1)
            
    print(len(neighbours),*neighbours)
    
    
