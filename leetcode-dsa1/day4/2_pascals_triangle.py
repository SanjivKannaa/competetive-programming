def generate(numRows):
    if numRows == 1:
        return  [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    l = [[1], [1, 1]]
    for i in range(numRows-2):
        print(l)
        l_ = [1]
        for j in range(len(l[-1])-1):
            l_.append(l[-1][j]+l[-1][j+1])
        l_.append(1)
        l.append(l_)
    return l