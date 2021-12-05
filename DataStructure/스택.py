import sys

count = int(sys.stdin.readline())
size = 0
stack = []

for _ in range(count):
    cmd = sys.stdin.readline().split()
    op = cmd[0]
    if op == "push":
        stack.append(int(cmd[1]))
        size += 1
    elif op == "pop":
        if(size == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
            size -= 1
    elif op == "size":
        print(size)
    elif op == "empty":
        if(size == 0):
            print(1)
        else:
            print(0)
    elif op == "top":
        if(size == 0):
            print(-1)
        else:
            print(stack[-1])