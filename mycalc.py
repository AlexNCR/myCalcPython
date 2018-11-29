import myfunc

print ("Welcome to my Math calculator on Python # Version 1.0")

while True:
    print("Options: ")
    print("Enter '+, add or Add' to add two numbers")
    print("Enter '-, substract or Substract' to substract two numbers")
    print("Enter '*, multiply or Multiply' to multiply two numbers")
    print("Enter '/, devide or Devide' to devide two numbers")
    print("Enter 'sqrt or SQRT' to take sqrt from number")
    print("Enter '**, power or Power' to degree number")
    print("Enter 'x, quit or Quit' to quit the program")
    user_input = input(": ")

    if user_input == "quit" or user_input == "Quit" or user_input == "x":
        break
    elif user_input == "+" or user_input == "add" or user_input == "Add":
        myfunc.MyMath.add_func()
    elif user_input == "-" or user_input == "substract" or user_input == "Substract":
        myfunc.MyMath.sub_func()
    elif user_input == "*" or user_input == "multiply" or user_input == "Multiply":
        myfunc.MyMath.mul_func()
    elif user_input == "/" or user_input == "devide" or user_input == "Devide":
        myfunc.MyMath.dev_func()
    elif user_input == "sqrt" or user_input == "SQRT":
        myfunc.MyMath.sqrt_func()
    elif user_input == "**" or user_input == "degree" or user_input == "Degree":
        myfunc.MyMath.power_func()
    else:
        print("Unknown input")
