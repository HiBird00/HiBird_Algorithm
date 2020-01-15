def merge(list1, list2):
    first = 0
    second = 0
    result = []
    while True:
        if first == len(list1):
            result.extend(list2[second:])
            break
        elif second == len(list2):
            result.extend(list1[first:])
            break
            
        if list1[first] <= list2[second]:
            small = list1[first]
            first += 1
        else:
            small = list2[second]
            second += 1
        result.append(small)
    
    return result
            
# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
    
    mid = len(my_list) // 2

    left_list = merge_sort(my_list[:mid])
    right_list = merge_sort(my_list[mid:])
    
    return merge(left_list, right_list)
    

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
