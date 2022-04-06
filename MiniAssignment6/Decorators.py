def multiply_div(func):
    def inner1(num1,num2):
        print("inner function" , num1*num2)
        func(num1,num2)

    return inner1

@multiply_div
def multiply(num1, num2):
    print(num1 * num2)
multiply(3,4)