# Ввод чисел
num1 = int (input ("Enter your first number  "))
num2 = int (input ("Enter your Second number (must be greater then first)  "))
if num2 <= num1:
    print ("Your second number less then first please change your number  ")
    num2 = int(input("Enter your Second number (must be greater then first)  "))
else:
    print ("Your numbers are accepted")

while num2 > num1:
    print ("Good job")
    num2 -= 1
# Проверка на букву А
name = str (input ("Enter your name:  "))
A = 0
for i in name:
    if i == "A":
        A += 1
if A > 0:
    print ("Your name contains letter \"A\"")
else:
    print("Your name not contains letter \"A\"")





