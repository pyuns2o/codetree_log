a, b = map(int, input().split())

# Write your code here!

def test(a,b):
    cnt = 0
    for num in range(a,b+1):
        if num % 3 == 0:
            cnt += 1
        else:
            s = str(num)
            for i in s:
                if (i=='3') or (i=='6') or (i=='9'):
                    cnt += 1
                    break
    return cnt

print(test(a,b))

