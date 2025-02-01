a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!

def add(a,c):
    print(a,"+", c,"=", a+c)

def diff(a,c):
    print(a,"-", c,"=",a-c)

def multiple(a,c):
    print(a,"*", c,"=",a * c)

def divide(a,c):
    print(a,"/", c,"=",a//c)

if o == '+':
    add(a,c)
elif o == '-':
    diff(a,c)
elif o =='*':
    multiple(a,c)
elif o == "/":
    divide(a,c)
else:
    print(False)