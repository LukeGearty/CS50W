import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot Divide By Zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")