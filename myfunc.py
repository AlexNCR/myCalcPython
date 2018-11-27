import math

class MyMath:
    def add_func():
        a1 = float(input("Input first number: "))
        a2 = float(input("Input second number: "))
        result = str(a1 + a2)
        print("Result is: " + result)

    def sub_func():
        a1 = float(input("Input first number: "))
        a2 = float(input("Input second number: "))
        result = str(a1 - a2)
        print("Result is: " + result)
    def mul_func():
        a1 = float(input("Input first number: "))
        a2 = float(input("Input second number: "))
        result = str(a1 * a2)
        print("Result is: " + result)
    def dev_func():
        a1 = float(input("Input first number: "))
        a2 = float(input("Input second number: "))
        result = str(a1 / a2)
        print("Result is: " + result)

    def sqrt_func():
        a1 = float(input("Input your number: "))
        result = str(math.sqrt(a1))
        print("Result is: " + result)

    def power_func():
        a1 = float(input("Input your number: "))
        a2 = float(input("Input your power: "))
        result = str(math.pow(a1, a2))
        print("Result is: " + result)
        
