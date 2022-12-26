# Enter your code here. Read input from STDIN. Print output to STDOUT
engSubCount = int(input())
engSubs = input().split()
frenchSubCount = int(input())
frenchSubs = input().split()
engSubs = set(engSubs)
frenchSubs = set(frenchSubs)
union = engSubs.union(frenchSubs)
print(len(union))
