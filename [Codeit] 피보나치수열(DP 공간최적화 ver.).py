def fib_optimized(n):
    # 코드를 작성하세요. 
    previous = 1
    current = 1
    for n in range(n-2):
        current, previous = current+ previous, current
        
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
