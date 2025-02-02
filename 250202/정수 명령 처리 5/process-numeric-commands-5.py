N = int(input())

temp = list()

for _ in range(N):
    command = input()

    if command.startswith("push_back"):
        _, num = tuple(command.split())
        temp.append(int(num))
    elif command.startswith("pop_back"):
        temp.pop()
    elif command.startswith("size"):
        print(len(temp))
    else:
        _, idx = tuple(command.split())
        print(temp[int(idx)-1])