testCount = int(input())
value = {}
value["S"] = 0
value["M"] = 1
value["L"] = 2
for i in range(testCount):
    left,right = input().split()
    if value[left[-1]] > value[right[-1]]:
        print(">")
    elif value[left[-1]] < value[right[-1]]:
        print("<")
    else:
        if left[-1] == "M" or len(left) == len(right):
            print("=")
        elif left[-1] == "S":
            if len(left)>len(right):
                print("<")
            elif len(left)<len(right):
                print(">")
        elif right[-1] == "L":
            if len(left)<len(right):
                print("<")
            elif len(left)>len(right):
                print(">")
        
    
