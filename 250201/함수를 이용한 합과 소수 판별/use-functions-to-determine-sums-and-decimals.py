a, b = map(int, input().split())

# Write your code here!

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_even(m):
    list = []
    s = str(m)
    for i in s:
        temp = int(i)
        list.append(temp)
    summ = sum(list)
    if summ % 2 == 0 :
        return True
    else:
        return False
    
cnt = 0
for i in range(a, b+1):
    if is_prime(i) == True and is_even(i)==True:
        cnt += 1

print(cnt)