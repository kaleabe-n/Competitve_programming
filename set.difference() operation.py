# Enter your code here. Read input from STDIN. Print output to STDOUT
engTotal = int(input())
engStud = input().split()
engStud = set(engStud)
frenchTotal = int(input())
frenchStud = input().split()
frenchStud = set(frenchStud)
engOnly = engStud.difference(frenchStud)
print(len(engOnly))
