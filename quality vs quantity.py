for i in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    i = 1
    j = len(nums)-1
    printed = False
    sumBlue = nums[0]
    sumRed = 0
    while i < j:
        sumBlue+=nums[i]
        sumRed+=nums[j]
        if sumRed>sumBlue:
            printed = True
            print("YES")
            break
        i+=1
        j-=1
    if not printed:
        print("NO")
