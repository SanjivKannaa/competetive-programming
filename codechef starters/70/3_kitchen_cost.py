for __ in range(int(input())):
    n, x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    cost = 0
    for i in range(n):
        if a[i] >= x:
            cost += b[i]
    print(cost)