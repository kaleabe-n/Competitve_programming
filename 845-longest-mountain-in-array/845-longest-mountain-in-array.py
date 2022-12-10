class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        state = None
        prev = None
        i = 0
        count = 0
        maxx = 0
        while i <len(arr):
            if state is None:
                if i == 0:
                    prev = arr[i]
                elif arr[i]>prev :
                    state = 'u'
                    count = 2
                elif arr[i]<prev :
                    state = 'd'
            elif state == "u":
                if arr[i] > prev:
                    count+=1
                elif arr[i] < prev:
                    count+=1
                    state = "ud"
                    maxx = max(count,maxx)
                else:
                    state = None
                    count = 0
            elif state == "d":
                if arr[i]>prev:
                    state = "u"
                    count = 2
                elif arr[i]==prev:
                    state = None
            elif state == "ud":
                if arr[i]<prev:
                    count+=1
                    maxx = max(maxx,count)
                elif arr[i]>prev:
                    count = 2
                    state = "u"
                else:
                    state = None
            prev = arr[i]
            i+=1
        return maxx