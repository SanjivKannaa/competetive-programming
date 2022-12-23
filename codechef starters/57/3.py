def func(l):
    count = 0
    for i in l:
        if i == 0:
            print("0")
            return 0
        if i<0:
            count += 1
    if count%2 != 0:
        print("1")
        return 0
    print("0")

for _ in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    func(l)