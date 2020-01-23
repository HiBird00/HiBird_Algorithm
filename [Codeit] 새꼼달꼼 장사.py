def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.    
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]
    
    if count in cache:
        return cache[count]

    maxCount = len(price_list) -  1
    if count > maxCount:
        cache[count] = max_profit_memo(price_list, count - 1, cache) + max_profit_memo(price_list, 1, cache)
    else:
        cache[count] = price_list[count]
        
    n = 1
    while count - n >= n:
            cache[count] = max(cache[count], max_profit_memo(price_list, count - n, cache) + max_profit_memo(price_list, n, cache))
            n += 1
            
    return cache[count]
    
def max_profit(price_list, count):
    max_profit_cache = {}
    
    return max_profit_memo(price_list, count, max_profit_cache)

# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
