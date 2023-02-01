for __ in range(int(input())):
    n = int(input())
    l = input()
    # print(l)
    s = 0
    for i in range(n):
        if l[i] == "1":
            s += 1
    

    if s<n/2:
        print(">>"+str(s))
    else:
        print(">>"+str(s+1))
