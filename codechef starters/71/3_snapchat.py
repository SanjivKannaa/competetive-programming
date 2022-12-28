for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    streak = 0
    max = 0
    for i in range(n):
        if (a[i]==0 or b[i]==0):
            if max<streak:
                max = streak
            streak = 0;
        else:
            streak+=1
    if max<streak:
        max = streak
    print(max)