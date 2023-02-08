def ispalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1]:
            return False
    return True

for __ in range(int(input())):
    n = int(input())
    s = input()
    val = False
    for i in range(len(s)):
        for j in range(1, len(s)):
            bruh = s[:i] + s[j:]
            # print(bruh)
            if ispalindrome(bruh):
                val = True
                print(">>>>" + str(j-i+1))
    if val == False:
        print(">>>" + str(-1))