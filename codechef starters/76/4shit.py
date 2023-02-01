for __ in range(int(input())):
    n = int(input())
    l = input()
    # print(l)
    s = 0
    for i in range(n):
        if l[i] == "0":
            s += 1
    
    if s==n:
        print(0)
    elif s<n/2:
        print(s+1)
    else:
        print(s)
