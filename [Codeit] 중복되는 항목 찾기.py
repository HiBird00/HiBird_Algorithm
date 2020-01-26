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

#------------------------------------------------------------------------------#

# 코드잇 해설
# 시간 복잡도 : O(n)
def find_same_number(some_list):
    # 코드를 쓰세요
    # 확인한 요소를 저장하는 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True
        

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

