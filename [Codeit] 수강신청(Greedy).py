def course_selection(course_list):
    # 코드를 작성하세요.
    pick_list = []
    course_list.sort(key=lambda t:t[1])
    
    # 가장 먼저 끝나는 수업 듣기
    pick_list.append(course_list[0])
    
    for end_time in course_list:
        if pick_list[-1][1] <= end_time[0]:
            pick_list.append(end_time)

    return pick_list
    


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
