n, m = map(int, input().split())

# Write your code here!

def lcm(n,m):
    gcd = 0
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    return (n * m) // gcd

print(lcm(n, m))
