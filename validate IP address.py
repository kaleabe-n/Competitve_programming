class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if isIpv4(queryIP):
            return "IPv4"
        elif isIpv6(queryIP):
            return "IPv6"
        return "Neither"
def isIpv4(ip):
    values = ip.split('.')
    if len(values)!=4:
        return False
    for val in values:
        if val.isdigit() and int(val)<256 and not(val[0]=='0' and len(val)!=1):
            continue
        else:
            return False
    return True

def isIpv6(ip):
    values = ip.split(":")
    if len(values)!=8:
        return False
    for val in values:
        if val.isalnum() and  1<=len(val)<=4:
            for letter in val:
                if letter.isdigit() or ord('a')<=ord(letter)<=ord('f') or ord('A')<=ord(letter)<=ord('F'):
                    continue
                else:
                    break
            else:
                continue
            return False
        else:
            return False
    return True
