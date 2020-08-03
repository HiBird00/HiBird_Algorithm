def boardCover(board):
    x = -1
    y = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                x = j
                y = i
                break
        if not y == -1:
            break
    # 모든 값을 다 채움
    if y == -1:
        return 1
    ret = 0
    for type in range(4):
        # 덮기
        if set(board, x, y, type, 1):
           ret += boardCover(board)
        set(board, x, y, type, -1)
    return ret

# delta = 1 : 덮음 / -1 : 지움
def set(board, x, y, type, delta):
    ok = True
    temp = True
    for i in range(3):
        nextX = x + coverType[type][i][1]
        nextY = y + coverType[type][i][0]
        # 범위 확인
        if nextX < 0 or nextX > len(board[0])-1 or nextY < 0 or nextY > len(board)-1:
            ok = False
            temp = False
        elif board[nextY][nextX] + delta > 1:
            ok = False
        if temp:
            board[nextY][nextX] += delta

    return ok


c = input()
c = int(c)
for num in range(c):
    h, w = input().split()
    h = int(h)
    w = int(w)
    board = [[0]*w for row in range(h)]
    # (y,x)
    coverType = [[[0,0],[0,1],[1,0]],
                 [[0,0],[1,0],[1,1]],
                 [[0,0],[0,1],[1,1]],
                 [[0,0],[1,0],[1,-1]]]
    # row 입력
    for i in range(h):
        row = input()
        row = row.replace('#', '1')
        row = row.replace('.', '0')
        for j in range(len(row)):
            board[i][j] = int(row[j])

    print(boardCover(board))



# 3차원 배열을 처음 써보았다.
# 이와같은 문제에서는 게임판을 덮을 수 있는 경우의 수를 네 타입별로 나누어 사용하였다. 새로운 방법에 신기했다.
# 파이썬은 알고리즘에 사용하기 조금 불편한 것 같다. int도 매번 변경해줘야하고.... 방법을 알아봐야겠다.
# 1~2년 전, 재귀를 처음 접했을 때는 뭐가 뭔지 1도 몰랐다. 지금도 여전히 어렵지만 조금씩 이해도가 높아지는게 느껴진다.
# 알고리즘. 이제 시작이고, 많이 실력이 부족하지만 1년동안 꾸준히 공부하면 내년엔 코딩테스트를 볼 수 있겠지?
# 파이팅. 김수현!
