for __ in range(int(input())):
    l = [int(i) for i in input().split()]
    if(l[0]>10*l[1]):
        print("YES")
    else:
        print("NO")