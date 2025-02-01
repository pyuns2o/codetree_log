n = int(input())

# Write your code here!

## try1
# def test(n):
#     if n % 2 != 0:
#         print("No")
#     else:
#         a = n // 10
#         b = n % 10
#         if (a+b) % 5 != 0:
#             print("No")
#         else:
#             print("Yes")

# test(n)

##try2
def test(n):
    if n%2==0 and ((n//10) + (n % 10)) % 5 == 0 :
        print("Yes")
    else:
        print("No")

test(n)