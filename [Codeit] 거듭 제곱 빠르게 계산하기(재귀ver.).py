# 시간 복잡도 : lg(y)
def power(x, y):
    # 코드를 작성하세요.
    if y == 1:
        return x
    
    # y가 홀수
    if y % 2 != 0:
        return x * power(x, y // 2) * power(x, y // 2)
    
    return power(x, y // 2) * power(x, y // 2)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
