# cook your dish here
for __ in range(int(input())):
    n, x = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if l[i]%2==0:
            count += 1
    print(count)