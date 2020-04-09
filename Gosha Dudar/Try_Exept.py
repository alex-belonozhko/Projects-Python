def FunkDivide ():
    print ("Enter first number")
    try:
        x = int ( input ())
    except ValueError:
        print ("You must input only number")
        x = 0
    else:
        print ("Your number accepted")

    print ("Enter second number")

    try:
        y = int ( input ())
    except ValueError:
        print ("You must input only number")
        y = 0
    else:
        if y != 0:
            print ("Your number accepted")
        else:
            print("Your number will make an error")
    # finally:
    #     print ("Good")

    try:
        div = x / y
    except ZeroDivisionError:
        print ("You cant divide by zero")
        div = 0
    # else:
    #     print ("result = ", div)

    return div

result_divide = FunkDivide()
print ("result = ", result_divide)