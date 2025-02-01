a, b = map(int, input().split())

# Write your code here!

# 소수 판별 함수 True/ False
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 소수 합산. True 이면 합산
summ = 0
for i in range(a, b+1):
    if is_prime(i):
        summ += i
        
print(summ)