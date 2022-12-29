testCount = int(input())
for i in range(testCount):
    sLen = int(input())
    nums = input().split()
    s = input()
    mapping = {}
    for i in range(sLen):
        if nums[i] in mapping:
            if mapping[nums[i]] != s[i]:
                print("NO")
                break
        else:
            mapping[nums[i]] = s[i]
    else:
        print("YES")
