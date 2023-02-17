class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        prev = None
        count = 1
        for i in range(len(chars)):
            letter  = chars[i]
            if prev == letter:
                count += 1
            elif prev != letter:
                if count > 1:
                    c = str(count)
                    for num in c:
                        chars[left] = num
                        left += 1
                count=1
                    
                chars[left] = letter
                left += 1
            prev = letter
            # print(chars,letter,i)
        if count > 1:
            c = str(count)
            for num in c:
                chars[left] = num
                left += 1
        while len(chars) > left:
            chars.pop()
        return left
                    