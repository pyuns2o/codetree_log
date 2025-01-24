n, m = map(int, input().split())

# Write your code here!

def lcm(n,m):
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    return (n * m) // gcd

print(lcm(n, m))

# def gcd(n,m):
#     for i in range(min(n,m), 0, -1):
#         if n % i == 0 and m % i == 0:
#             return i
# def lcm(n,m):
#     return n * m // gcd(n,m)
    
# print(lcm(n,m))
