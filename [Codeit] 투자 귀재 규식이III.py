# 시간 복잡도 : o(n)
def sublist_max(profits):
    # 코드를 작성하세요.
    last_max = profits[0]
    max_so_far = profits[0]
    
    for i in range(1,len(profits)):
        # 마지막 값이 포함될 때의 최고 구간 값
        last_max = max(last_max + profits[i], profits[i])
        
        # 마지막이 포함되는 구간 값 vs 마지막이 포함되지 않을 때의 최대 구간 값
        max_so_far = max(max_so_far, last_max)
    
    return max_so_far
    
    
    
# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
