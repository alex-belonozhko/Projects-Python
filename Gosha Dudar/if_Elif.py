def YourAge():
    age = int (input ("Enter your age: "))
    if age > 0:
        if age == 18:
            print("now you are not a child")
        elif age < 18:
            print("You are a child")
        elif age > 18:
            print("You are an adult")
    elif age < 0:
        print("Ohh You are not born yet")
    else:
        print("Happy Birthday!!!")



