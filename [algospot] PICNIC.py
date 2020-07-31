def setPair(clear):
    firstcheck = -1
    for i in range(n):
        # 짝이 없다면
        if not clear[i]:
            firstcheck = i
            break
    # 다 짝이 있다면
    if firstcheck == -1:
        return 1
    ret = 0
    for pairIndex in range(firstcheck+1, n):
        # 둘이 짝이라면
        if friend[firstcheck][pairIndex]:
            if not clear[pairIndex]:
                clear[firstcheck] = clear[pairIndex] = True
                ret += setPair(clear)
                clear[firstcheck] = clear[pairIndex] = False
    return ret

# 테스트 케이스
c = int(input())
global n
global friend
for i in range(c):
    # 학생 수, 쌍
    n , m = input().split()
    n = int(n)
    m = int(m)
    friend = [[0]*n for row in range(n)]
    clear = [0 for i in range(n)]
    pair = [int(x) for x in input().split()]
    for j in range(0, m*2, 2):
        first = pair[j]
        second = pair[j+1]
        friend[first][second] = friend[second][first] = True

    print(setPair(clear))








