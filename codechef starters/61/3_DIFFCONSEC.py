# cook your dish here
from typing import Counter


for __ in range(int(input())):
    input()
    s = list(input())
    count = 0
    prev = s[0]
    for i in range(1, len(s)):
        if prev == "0" and prev == s[i]:
            s[i] = "1"
            count += 1
        elif prev == "1" and prev == s[i]:
            s[i] = "0"
            count += 1
        prev = s[i]
    print(count)