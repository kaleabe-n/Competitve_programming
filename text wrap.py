def wrap(string, max_width):
    ans = []
    for i in range(len(string)):
        ans.append(string[i])
        if (i+1)%max_width == 0:
            ans.append("\n")
    return "".join(ans)

