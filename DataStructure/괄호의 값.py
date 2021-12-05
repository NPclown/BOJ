import sys

def correct(string):
    stack = []
    for s in string:
        if s in dictionary.values():
            stack.append(s)
        else:
            if stack == [] or dictionary[s] != stack.pop():
                return False

    return True if stack == [] else False

def value(string):
    stack = []
    for s in string:
        if s in dictionary.values():
            stack.append(s)
        elif s == ')':
            tmp = 0
            while(stack[-1] != '('):
                tmp += stack.pop()
            stack.pop()
            stack.append(2 if tmp == 0 else 2 * tmp)
        elif s == ']':
            tmp = 0
            while(stack[-1] != '['):
                tmp += stack.pop()
            stack.pop()
            stack.append(3 if tmp == 0 else 3 * tmp)
    return sum(stack)

str1 = sys.stdin.readline().strip()
dictionary = {')':'(', ']':'['}

if correct(str1):
    print(value(str1))
else:
    print(0)