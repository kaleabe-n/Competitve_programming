# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
aIndices = defaultdict(list)
aCount,bCount = input().split()
aCount = int(aCount)
bCount = int(bCount)
for i in range(aCount):
    word = input()
    aIndices[word].append(str(i+1))
for _ in range(bCount):
    word = input()
    if not aIndices[word]:
        print(-1)
    else:
        print(" ".join(aIndices[word]))
