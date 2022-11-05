#Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x, y):
    return x / y

# this function quest next_calculation
def quest():
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
        request()
    elif next_calculation.lower() == "yes":
        return
    else:
        quest()

# This function request next_calculation
def request():
    re_next_calculation = input("Are you sure? (yes/no): ")
    if re_next_calculation.lower() =="yes":
        exit()
    elif re_next_calculation.lower() == "no":
        quest()
    else:
        request()