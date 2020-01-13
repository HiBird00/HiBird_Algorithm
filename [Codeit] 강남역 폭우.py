def findRain(buildings):
    result = 0
    big_index = 0
    start_index = 0
    stop_index = 1
    
    while stop_index < len(buildings):
        if buildings[start_index] > buildings[stop_index]:
            result += buildings[big_index] - buildings[stop_index]
            start_index += 1
            stop_index += 1
        else:
            if buildings[big_index] >= buildings[stop_index]:
                result += buildings[big_index] - buildings[stop_index]
            else:
                big_index = stop_index
            start_index += 1
            stop_index += 1
    return result

def trapping_rain(buildings):
    # 코드를 작성하세요
    biggest_index = buildings.index(max(buildings))
    left_buildings = buildings[:biggest_index+1]
    right_buildings = buildings[biggest_index:]
    right_buildings.reverse()
    
    return findRain(left_buildings) + findRain(right_buildings)
    
                
                

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

