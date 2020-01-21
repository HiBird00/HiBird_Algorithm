def max_profit(price_list, count):
    # 코드를 작성하세요. 
    table = [0 for i in range(count+1)]
    table[0] = price_list[0]
    table[1] = price_list[1]
    for i in range(2, count+1):
        if i <= len(price_list) - 1:
            table[i] = price_list[i]
        n = 1
        while i - n >= n:
            table[i] = max(table[i], table[i-n] + table[n])
            n += 1
    return table[count]
        
# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
