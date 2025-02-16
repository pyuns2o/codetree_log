n = int(input())
l = list(map(int, input().split()))

for i in range(n-1):
    mini = i
    for j in range(i+1, n):
        if l[j] < l[mini]:
            mini = j
    temp = l[i]
    l[i] = l[mini]
    l[mini] = temp

for num in l:
    print(num, end=' ')