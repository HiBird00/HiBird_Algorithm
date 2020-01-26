# 시간 복잡도 : O(nlogn)
def find_same_number(some_list):
    # 코드를 쓰세요
    # 리스트를 오름차순으로 정렬
    some_list.sort()
    for i in range(len(some_list)-1):
        if some_list[i+1] == some_list[i]:
            break
    return some_list[i]
        

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
