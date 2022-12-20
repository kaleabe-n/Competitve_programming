def swap_case(s):
    ans = ""
    for i in s:
        if ord('z') >= ord(i) >= ord('a'):
            ans+=chr(ord(i)-32)
        elif ord('Z') >= ord(i) >= ord('A'):
            ans+=chr(ord(i)+32)
        else:
            ans+=i
    return ans
