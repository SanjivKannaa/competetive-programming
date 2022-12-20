def firstUniqChar(s):
    l = []
    for i in range(len(s)):
        if s[i] in l:
            continue
        for j in range(len(s)):
            if j<=i:
                continue
            if s[i] == s[j]:
                l.append(s[i])
                break
            if j == len(s)-1:
                return i
        if i == len(s)-1:
            return i
    if len(s)==1:
        return 0
    return -1