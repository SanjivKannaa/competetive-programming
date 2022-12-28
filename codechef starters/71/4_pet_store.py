for __ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    ret="YES"
    bruh = []
    for i in l:
        if i not in bruh and l.count(i)%2!=0:
            ret = "NO"
            break
        bruh.append(i)
    if ret=="YES":
        print("YES")
    else:
        print("NO")