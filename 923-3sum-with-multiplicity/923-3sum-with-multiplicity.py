class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = defaultdict(lambda :0)
        ans=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                ans+=count[target-(arr[i]+arr[j])]
            count[arr[i]]+=1
        return ans%(10**9+7)
                    