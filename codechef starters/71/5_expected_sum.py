from itertools import permutations as p

def f(i):
    if i%1>=0.5:
        return int(i)+1
    return int(i)

for __ in range(int(input())):
    a = [int(i) for i in input().split()]
    n = a[0] + a[1]
    l = [1]*a[0]
    l.extend([0]*a[1])
    print(list(p(l)))
    sum_ = 0
    number_of_p = 0
    for i in list(p(l)):
        number_of_p += 1
        for j in range((n//2)):
            sum_ += int(i[j])
    print(sum_, number_of_p)
    sum_ = sum_/number_of_p
    # print(sum_, number_of_p)
    print(f(998244353 * sum_))