def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    stops = []
    pre_dis = 0
    
    for i in range(len(water_stops)):
        # 해당 약수터까지 못 올라간다면, 그 전 약수터를 들린다
        if water_stops[i] - pre_dis > capacity:
            pre_dis = water_stops[i - 1]
            stops.append(pre_dis)
    stops.append(water_stops[-1])
    
    return stops
    
# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
