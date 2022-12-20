# cook your dish here
for __ in range(int(input())):
    count = [0, 0]
    l = [int(i) for i in input().split()]
    for i in range(3):
        if l[i]%2 == 0:
            count[1] += 1
        else:
            count[0] += 1
    if count[0] == 0 or count[1] == 0:
        print("NO")
    else:
        print("YES")