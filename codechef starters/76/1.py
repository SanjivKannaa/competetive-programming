# cook your dish here
for __ in range(int(input())):
    n, x, y = [int(i) for i in input().split()]
    if x*y>=n:
        print("YES")
    else:
        print("NO")