n = int(input())


# Write your code here!
def print_func(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num += 1
            if num == 10:
                num = 1
        print()

print_func(n)
