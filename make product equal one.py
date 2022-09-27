count = input()
nums = [int(x) for x in input().split()]
hasZero = False
cost = 0
prod = 1
for i in range(len(nums)-1,-1,-1):
    if nums[i] == 0 :
        hasZero = True
        cost+=1
    elif nums[i]<0:
        cost+=abs(nums[i])-1
        prod*=-1
    else:
        cost+=nums[i]-1
if prod==-1:
    if not hasZero:
        cost+=2
print(cost)
