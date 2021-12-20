#mine VALLEY COUNTER

def valleyCounter(str):
    stack = []
    numberOfValleys=0
    for i in str:
        if((i=='u') and (len(stack) != 0) and (stack[-1]=='d')):
            stack.pop()
        elif(len(stack)==0 and i=='d'):
            stack.append('d')
            numberOfValleys+=1
        elif(len(stack)!=0 and i=='d' and stack[-1]=='u'):
            stack.pop()
        else:
            stack.append(i)
    return numberOfValleys
print(valleyCounter("UDDDUDUU"))
