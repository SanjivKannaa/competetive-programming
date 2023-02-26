word = ""
m = 3
div = [0]*len(word)
s=0
for i in range(len(word)):
    s = s*10 + int(word[i])
    if (s%m == 0):
        div[i] = 1
    else:
        div[i] = 0
# return div