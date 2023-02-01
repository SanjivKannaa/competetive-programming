# cook your dish here
for __ in range(int(input())):
    a, b, c = [int(i) for i in input().split()]
    s = a+b+c
    if s>=6:
        print("YES")
    else:
        print("NO")