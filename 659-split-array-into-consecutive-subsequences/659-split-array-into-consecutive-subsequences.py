class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        expect = {}
        for i in nums:
            if i in expect:
                if len(expect[i]) == 0:
                    expect[i+1].append([i])
                else:
                    temp = expect[i].pop()
                    temp.append(i)
                    if i+1 in expect:
                        expect[i+1].append(temp)
                        expect[i+1].sort(key = lambda x:-len(x))
                    else:
                        expect[i+1] = [temp]
            else:
                if i+1 in expect:
                    expect[i+1].append([i])
                else:
                    expect[i+1] = [[i]]
        for i in expect:
            for j in expect[i]:
                if 0<len(j)<=2:
                    return False
        return True
        