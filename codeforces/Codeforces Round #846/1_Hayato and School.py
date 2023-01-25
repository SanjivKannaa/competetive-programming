for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    odd = []
    even = []
    for i in range(n):
        if a[i]%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    