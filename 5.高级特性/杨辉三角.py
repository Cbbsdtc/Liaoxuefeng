def triangles(max):
    L = [1]
    while len(L) < (max+1):
        print(L)
        for i in range(1,len(L)):
            L[-i] = L[-i] + L[-i-1]
        L.append(1)
    return "done"

triangles(10)