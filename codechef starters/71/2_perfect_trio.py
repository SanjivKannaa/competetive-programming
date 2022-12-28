for __ in range(int(input())):
    l = [int(i) for i in input().split()]
    if (l[0] == l[1]+l[2] or l[1] == l[0]+l[2] or l[2] == l[1]+l[0]):
        print("YES")
    else:
        print("NO")