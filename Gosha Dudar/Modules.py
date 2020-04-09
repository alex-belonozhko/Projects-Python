# from Calc2Numbers import SayHello as H
# from if_Elif import YourAge
# from Calc2Numbers import multiplication
# from Calc2Numbers import addition
import datetime

date = datetime.datetime.today()
newdata = date - datetime.timedelta(1)
print(newdata.strftime('%Y-%m-%d %H.%M.%S'))

# print (multiplication(2, 6))
# print (addition(5, 2))
# YourAge ()
# H ()