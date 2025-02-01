n = int(input())

# Write your code here!

def test(n):
    if n % 2 != 0:
        print("No")
    else:
        a = n // 10
        b = n % 10
        if (a+b) % 5 != 0:
            print("No")
        else:
            print("Yes")

test(n)