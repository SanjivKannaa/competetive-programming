for __ in range(int(input())):
    n, c = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    for i in range(n//2+1):
        a[i] += i+1
    for i in range(n//2+1, n):
        a[i] += n-i
    # print(a)
    a.sort()
    count = 0
    for i in a:
        if c-i < 0:
            break
        c -= i
        count += 1
    print(">>"+str(count))