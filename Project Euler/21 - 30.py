# task#21

# Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
# Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.
# Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284.
# Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
# Подсчитайте сумму всех дружественных чисел меньше 10000.

# def SummDividersNumber(Number):
#     list = []
#     for i in range(1, Number):
#         if Number % i == 0:
#             list.append(i)
#     return sum(list)
#
# list = []
# SummFriendlyNumber = 0
# for Number in range(10000+1, 1, -1):
#     SummDivNumber = SummDividersNumber(Number)
#     if Number == SummDividersNumber(SummDivNumber):
#         if Number != SummDivNumber:
#             list.append(SummDivNumber)
#             if Number not in list:
#                 print(Number, " ", SummDivNumber)
#                 SummFriendlyNumber += (Number + SummDivNumber)
#
# print(SummFriendlyNumber)

# task#22

# Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
# текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в алфавитном порядке.
# Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном
# списке для получения количества очков имени.
# Например, если список отсортирован по алфавиту, имя COLIN
# (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке.
# Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
# Какова сумма очков имен в файле?

# dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
#         'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
#
# file = open('names.txt')
# ListOfNames = []
#
# for line in file.readlines():
#     if len(line) > 1:
#         for t in line.split(","):
#             ListOfNames.append(t)
# file.close()
# ListOfNames.sort()
#
# def TotalPointsName(ClearName, ListOfNames):
#     SummSymbol = 0
#     for Symbol in ClearName:
#         SummSymbol += dict[Symbol]
#     return SummSymbol * (ListOfNames.index(Name) + 1)
#
# TotalPointsListOfNames = 0
# for Name in ListOfNames:
#     ClearName = Name.strip('"')
#     TotalPointsListOfNames += TotalPointsName(ClearName, ListOfNames)
#
# print(TotalPointsListOfNames)

# task#24

# Перестановка - это упорядоченная выборка объектов. К примеру,
# 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4.
# Если все перестановки приведены в порядке возрастания или алфавитном порядке,
# то такой порядок будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
# 012   021   102   120   201   210
# Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

# import itertools
#
# list = [0,1,2,3,4,5,6,7,8,9]
# List = []
# a = set(itertools.permutations(list))
# for i in a:
#     List.append(i)
# List.sort()
# print(List[1000000-1])

# task#25

# Последовательность Фибоначчи определяется рекурсивным правилом:
# Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
# Таким образом, первые 12 членов последовательности равны:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
# Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?

# Pred = 1
# PredPred = 1
# list = [1, 1]
#
# while True:
#     Summ = Pred + PredPred
#     list.append(Summ)
#     PredPred, Pred = Pred, Summ
#     if len(str(Summ)) == 1000:
#         break
#
# print(list.index(Summ) + 1)

# task#27






