def merge_the_tools(string, k):
    l = len(string)
    res = []
    for i in range(0, l, k):
        w = list(string[i:i + k])
        for j in w:
            if j not in res:
                res.append(j)
        for o in res:
            print(o, end='')
        res.clear()
        print()
