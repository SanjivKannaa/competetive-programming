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
    if len(even) >= 2 and len(odd)>=1:
        print("YES")
        print(even[0]+1, even[1]+1, odd[0]+1)
    elif len(odd) >= 3:
        print("YES")
        print(odd[0]+1, odd[1]+1, odd[2]+1)
    else:
        print("NO")