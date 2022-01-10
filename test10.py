a = int(input())
b = int(input())


op = input()

if op =="+":
    result = a + b
if op =="-":
    result = a - b
if op =="*":
    result = a * b
if op == "/":
    if b != 0:
        result = a / b
    else:
        result = "cannot devide by zero"

print(result)