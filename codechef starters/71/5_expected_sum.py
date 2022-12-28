from itertools import permutations as p

for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    l = [1]*a[0]
    l.extend([0]*a[1])
    # print(l)
    number_of_p = 0
    for i in list(p(l)):
        number_of_p += 1
        