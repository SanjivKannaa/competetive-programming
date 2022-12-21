for __ in range(int(input())):
    n = int(input())
    b = [int(i) for i in input().split()]
    d = dict()
    a = []
    occured = []
    for i in range(n):
        if b[i] not in occured:
            # print(-1)
            d[len(d)+1] = [b[i], 1]
            a.append(len(d))
            occured.append(b[i])
        else:
            for j in list(d.keys()):
                if d[j][0] == b[i]:
                    if d[j][1]<=d[j][0]:
                        # print(0)
                        d[j][1] += 1
                        a.append(j)
                    else:
                        # print(1)
                        d[len(d)+1] = [b[i], 1]
                        a.append(len(d))
    #     print(d, occured)
    # print()
    # print()
    # print()
    val = 1
    for i in list(d.keys()):
        if d[i][0] != d[i][1]:
            val = 0
            print(-1)
            break
    if val:
        print(a)


# 5
# 5
# 2 3 3 3 2
# 5
# 1 1 1 1 1
# 5
# 5 5 5 5 5
# 3
# 1 2 4
# 8
# 1 3 2 3 2 2 2 3