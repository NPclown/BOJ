import sys
count = int(sys.stdin.readline())
answer = [int(sys.stdin.readline()) for _ in range(count)]

result = []
tmp = []

num = 1

for index in range(count):
    while num <= answer[index]:
        tmp.append(num)
        num += 1
        result.append("+")

    if tmp.pop() == answer[index]:
        result.append("-")
    else:
        result = ["NO"]
        break

print("\n".join(result))

#for i in result:
#    print(i)
#보다
#print("\n".join(result)) 더 빠르다. 70ms 정도
