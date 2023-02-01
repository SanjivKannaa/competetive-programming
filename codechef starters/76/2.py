# cook your dish here
for __ in range(int(input())):
    x, y, z = [int(i) for i in input().split()]
    m = min(min(x, y), z)
    if m == x:
        print("ALICE")
    elif m == y:
        print("BOB")
    elif m == z:
        print("CHARLIE")