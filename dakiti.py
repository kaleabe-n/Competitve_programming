testCount = int(input())
for i in range(testCount):
    words = input().split()
    ans = {}
    for word in words:
        temp = []
        currInd = []
        for letter in word:
            if ord("0")<=ord(letter) <= ord("9"):
                currInd.append(str(int(letter)))
            else:
                temp.append(letter)
        ind = int("".join(currInd))
        ans["".join(temp)] = ind
    ans = sorted(ans,key = lambda x:ans[x])
    print(" ".join(ans))
