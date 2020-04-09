#task Count Consecutive Summers

# Positive integers can be expressed as sums of consecutive positive integers in various ways. For example,
# 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.
# As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum that consists of that integer alone.
# Compute how many different ways it can be expressed as a sum of consecutive positive integers.

# def count_consecutive_summers(num):
#     ListNum = []
#     Count = 0
#     n = 1
#     while True:
#         for i in range(n,num+1):
#             ListNum.append(i)
#             if sum(ListNum) == num:
#                 Count += 1
#                 ListNum.clear()
#                 break
#             elif sum(ListNum) > num:
#                 ListNum.clear()
#                 break
#         n += 1
#         if n > num:
#             break
#     return Count
#
# if __name__ == '__main__':
#     print("Example:")
#     print(count_consecutive_summers(42))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert count_consecutive_summers(42) == 4
#     assert count_consecutive_summers(99) == 6
#     assert count_consecutive_summers(1) == 1
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Time Converter (12h to 24h)

# You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places.
# Your task is to convert the time from the 12-h format into 24-h by following the next rules:
# - the output format should be 'hh:mm'
# - if the output hour is less than 10 - write '0' before it. For example: '09:05'
# Here you can find some useful information about the 12-hour format.

# def time_converter(time):
#     ListTime = time.split()
#     ListHourMinute = ListTime[0].split(":")
#     hour = int(ListHourMinute[0])
#     if hour < 12:
#         if ListTime[1] == "p.m.":
#             return str(hour + 12) + ":" + ListHourMinute[1]
#         elif ListTime[1] == "a.m.":
#             return "0" + ':'.join(ListHourMinute)
#     elif hour == 12:
#         if ListTime[1] == "p.m.":
#             return ':'.join(ListHourMinute)
#         elif ListTime[1] == "a.m.":
#             return "00:" + ListHourMinute[1]

#Amazing code from answer

# def time_converter(time):
#     h, m = map(int, time[:-5].split(':'))
#     return f"{h % 12 + 12 * ('p' in time):02d}:{m:02d}"

# if __name__ == '__main__':
#     print("Example:")
#     # print(time_converter('12:30 p.m.'))
#     #
#     # #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert time_converter('12:30 p.m.') == '12:30'
#     assert time_converter('11:00 a.m.') == '09:00'
#     assert time_converter('11:15 p.m.') == '23:15'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Speech Module

# FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
#              "eight", "nine"]
# SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
#               "sixteen", "seventeen", "eighteen", "nineteen"]
# OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
#               "eighty", "ninety"]
# HUNDRED = "hundred"

#My code ( bad )

# def checkio(number):
#     StrNumber = str(number)
#     if len(StrNumber) == 1:
#         return FIRST_TEN[number - 1]
#     elif len(StrNumber) == 2:
#         if StrNumber[0] == "1":
#             return SECOND_TEN[int(StrNumber[1])]
#         else:
#             if StrNumber[1::] == "0":
#                 return OTHER_TENS[int(StrNumber[0]) - 2]
#             else:
#                 return OTHER_TENS[int(StrNumber[0]) - 2] + " " + FIRST_TEN[int(StrNumber[1]) - 1]
#     elif len(StrNumber) == 3:
#         if StrNumber[1::] == "00":
#             return FIRST_TEN[int(StrNumber[0]) - 1] + " " + HUNDRED
#         elif StrNumber[1::2] == "0":
#             return FIRST_TEN[int(StrNumber[0]) - 1] + " " + HUNDRED + " " + FIRST_TEN[int(StrNumber[2]) - 1]
#         elif StrNumber[2::] == "0":
#             return FIRST_TEN[int(StrNumber[0]) - 1] + " " + HUNDRED + " " + OTHER_TENS[int(StrNumber[1]) - 2]
#         elif StrNumber[1] == "1":
#             return FIRST_TEN[int(StrNumber[0]) - 1] + " " + HUNDRED + " " + SECOND_TEN[int(StrNumber[2])]
#         elif StrNumber[1] != "1":
#             return FIRST_TEN[int(StrNumber[0]) - 1] + " " + HUNDRED + " " + OTHER_TENS[int(StrNumber[1]) - 2] + " " + FIRST_TEN[int(StrNumber[2]) - 1]

#Code from internet

# def checkio(number):
#
#     n = number // 100
#     t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []
#
#     n = (number // 10) % 10
#     t += [OTHER_TENS[n-2]] if n > 1 else []
#
#     n = number % (10 if n > 1 else 20)
#     t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []
#
#     return ' '.join(t)
#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(207) == 'four', "1st example"
#     assert checkio(133) == 'one hundred thirty three', "2nd example"
#     assert checkio(12) == 'twelve', "3rd example"
#     assert checkio(101) == 'one hundred one', "4th example"
#     assert checkio(212) == 'two hundred twelve', "5th example"
#     assert checkio(40) == 'forty', "6th example"
#     assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
#     print('Done! Go and Check it!')

#task Find Sequence

# You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits.
# The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

#My code YYYEEEAAA I DID THIS

#from itertools import groupby

# def Funkgroupby(list):
#     for k, g in groupby(list):
#         if sum(1 for _ in g) >= 4:
#             return True
#
# def checkio(matrix):
#     for i in matrix:
#         for k, g in groupby(i):
#             if sum(1 for _ in g) >= 4:
#                 return True
#     list = []
#     n = 0
#     while True:
#         for j in matrix:
#            list.append(j[n])
#         if Funkgroupby(list):
#             return True
#         list.clear()
#         if n == len(matrix) - 1:
#             break
#         n += 1
#
#     n = 0
#     ListReserve = []
#     LenMatrix = len(matrix) - 4
#     for i in range(LenMatrix):
#         ListReserve.append(matrix[0])
#         del matrix[0]
#     while True:
#         k = n
#         if len(matrix) > 3:
#             for j in matrix:
#                 list.append(j[k])
#                 k += 1
#                 if k == -1:
#                     break
#                 else:
#                     if k == len(j):
#                         break
#             if Funkgroupby(list):
#                 return True
#             if len(list) < 4:
#                 break
#             list.clear()
#             if ListReserve:
#                 matrix.insert(0, ListReserve[-1])
#                 del ListReserve[-1]
#             else:
#                 n += 1
#     n = 3
#     while True:
#         k = n
#         for j in matrix:
#             list.append(j[k])
#             k -= 1
#             if k == -1:
#                 break
#         if Funkgroupby(list):
#             return True
#         if len(list) < 4:
#             break
#         list.clear()
#         if len(matrix) - 1 > n:
#             n += 1
#         else:
#             del matrix[0]
#     return False

#Code from internet which i dont understand )))

# def checkio(matrix):
#     N = len(matrix)
#     def seq_len(x, y, dx, dy, num):
#         if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
#             return 1 + seq_len(x + dx, y + dy, dx, dy, num)
#         else:
#             return 0
#
#     DIR = [(dx, dy) for dy in range(-1, 2)
#                     for dx in range(-1, 2)
#                     if dx != 0 or dy != 0]
#     for y in range(N):
#         for x in range(N):
#             for dx, dy in DIR:
#                 if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
#                     return True
#     return False

# if __name__ == '__main__':
#     assert checkio([
#         [1, 2, 1, 1],
#         [1, 1, 4, 1],
#         [1, 3, 1, 6],
#         [1, 7, 2, 5]
#     ]) == True, "Vertical"
#     assert checkio([
#         [7, 1, 4, 1],
#         [1, 2, 5, 2],
#         [3, 4, 1, 3],
#         [1, 1, 8, 1]
#     ]) == False, "Nothing here"
#     assert checkio([
#         [2, 1, 1, 6, 1],
#         [1, 3, 2, 1, 1],
#         [4, 1, 1, 3, 1],
#         [5, 5, 5, 5, 5],
#         [1, 1, 3, 1, 1]
#     ]) == True, "Long Horizontal"
#     assert checkio([
#         [7, 1, 1, 8, 1, 1],
#         [1, 1, 7, 3, 1, 5],
#         [2, 3, 1, 2, 5, 1],
#         [1, 1, 1, 5, 1, 4],
#         [4, 6, 5, 1, 3, 1],
#         [1, 1, 9, 1, 2, 1]
#     ]) == True, "Diagonal"

#task Multicolored Lamp

# Your task is to create the class Lamp() and method light() which will make the lamp glow with one
# of the four colors in the sequence - (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’). When the light() method is used for the first time,
# the color should be 'Green', the second time - 'Red' and so on. If the current color is 'Yellow', the next color should be 'Green' and so on.
# In this mission you can use the State design pattern.
# It's highly useful in the situations where object should change its behaviour depending on the internal state.

# import itertools
#
# class Lamp():
#     Sequence = ('Green', 'Red', 'Blue', 'Yellow')
#     def __init__(self):
#         self.color = itertools.cycle(Lamp.Sequence)
#
#     def light(self):
#         return next(self.color)
#
# if __name__ == '__main__':
#
#     lamp_1 = Lamp()
#     lamp_2 = Lamp()
#
#     lamp_1.light()  # Green
#     lamp_1.light()  # Red
#     lamp_2.light()  # Green
#
#     assert lamp_1.light() == "Blue"
#     assert lamp_1.light() == "Yellow"
#     assert lamp_1.light() == "Green"
#     assert lamp_2.light() == "Red"
#     assert lamp_2.light() == "Blue"
#     print("Coding complete? Let's try tests!")

#task Brackets

# You are given an expression with numbers, brackets and operators.
# For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".
# Brackets are used to determine scope or to restrict some expression. If a bracket is open,
# then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket.
# In this task you should make a decision,
# whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

# 1 method ( more shord )

# def checkio(data):
#     stack = [""]
#     brackets = {"(":")","[":"]","{":"}"}
#     for c in data:
#         if c in brackets:
#             stack.append(brackets[c])
#         elif c in brackets.values() and c != stack.pop():
#             return False
#     return stack == [""]
# def checkio(data):

# 2 method ( more clear )

#     stack = [""]
#     brackets = {"(":")","[":"]","{":"}"}
#     for c in data:
#         if c in brackets:
#             stack.append(brackets[c])
#         elif c in brackets.values() and c == stack[len(stack) - 1]:
#             stack.pop()
#         elif c in brackets.values() and c != stack[len(stack) - 1]:
#             return False
#     return stack == [""]

# if __name__ == '__main__':
#     assert checkio("((5+3)*2+1)") == True, "Simple"
#     assert checkio("{[(3+1)+2]+}") == True, "Different types"
#     assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
#     assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#     assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#     assert checkio("2+3") == True, "No brackets, no problem"

# task Probably Dice

# напишите функцию, которая принимает на вход число кубиков, число сторон на кубике и исследуемый номер,
# а возвращает вероятность получения заданного значения.
# Результат должен возвращаться с точностью в четыре цифры после запятой - ±0.0001.

# Выполнил по сути задание, считает до 4 кубиков включитено. А дальше не правильно, но ХЗ на сайте написано что должна тенденция
# сохраняться а она по видимому не сохраняеться

# def FillDict(matrix, dice_number, sides, k = 0, t = True, Percent = 0):
#     Value = dice_number
#     dict = {}
#     while t == True:
#         g = k
#         for i in matrix:
#             Percent += i[g]
#             g -= 1
#             if g == -1:
#                 break
#         dict[Value] = Percent
#         if Value != dice_number * sides:
#             Value += 1
#         else:
#             break
#         Percent = 0
#         if k < sides - 1:
#             k += 1
#         else:
#             del matrix[0]
#     return dict
#
# def probability(dice_number, sides, target):
#     Chanсe = (1/sides**2) * 100
#     matrix = []
#     for i in range(sides):
#         matrix.append([Chanсe for j in range(sides)])
#
#     dict = FillDict(matrix, 2, sides)
#
#     if dice_number > 2:
#         MaxDictValue = max(dict.values())
#         for j in dict:
#             dict[j] = dict[j] / 100 * MaxDictValue
#         matrix = []
#         DiceNumber = dice_number
#         for DiceNumber in range(3, dice_number + 1):
#             matrix = []
#             for value in dict.values():
#                 matrix.append([value for j in range(sides)])
#             dict = FillDict(matrix, DiceNumber, sides)
#             if DiceNumber != dice_number:
#                 MaxDictValue = max(dict.values())
#                 for j in dict:
#                     dict[j] = ((dict[j] / 100) * (16.67 / 100)) * 100
#             else:
#                 if target in dict:
#                     return round(dict[target] / 100, 4)
#                 else:
#                     return 0.0000
#     else:
#         if target in dict:
#             return round(dict[target] / 100, 4)
#         else:
#             return 0.0000
#

#code from internet

# from numpy.polynomial.polynomial import polypow
#
#
# def probability(dice_number, sides, target):
#     powers = [0] + [1] * sides
#     poly = polypow(powers, dice_number)
#     try:
#         return poly[target] / sides ** dice_number
#     except IndexError:
#         return 0


# if __name__ == '__main__':
#     # These are only used for self-checking and are not necessary for auto-testing
#     def almost_equal(checked, correct, significant_digits=4):
#         precision = 0.1 ** significant_digits
#         return correct - precision < checked < correct + precision
#
#
#     assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
#     assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
#     assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
#     assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
#     assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
#     assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
#     assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

#task Roman Numerals

#В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.

#my code

# def funk(data):
#     for value in [(data // 100) % 10, (data // 10) % 10, data % 10]:
#         yield value
#
# def checkio(data):
#     dict = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"}
#     generator = funk(data)
#     t = ""
#     k = "00"
#     n = data // 1000
#     t += dict[1000] * n if n > 0 else ""
#     for i in range(3):
#         n = next(generator)
#         if n >= 5:
#             if n < 9:
#                 t += dict[int(str(5) + k)] + (dict[int(str(1) + k)] * (n - 5))
#             else:
#                 t += dict[int(str(1) + k)] + dict[int(str(10) + k)]
#         else:
#             if n == 4:
#                 t += dict[int(str(1) + k)] + dict[int(str(5) + k)]
#             else:
#                 t += dict[int(str(1) + k)] * n if n > 0 else ""
#         if k:
#             k = k[1::]
#     return t

#The best code from genious

# def checkio(n):
#     result = ''
#     for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
#                              'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
#         result += n // arabic * roman
#         n %= arabic
#     return result
#
# if __name__ == '__main__':
#
#     # assert checkio(6) == 'VI', '6'
#     # assert checkio(76) == 'LXXVI', '76'
#     # assert checkio(499) == 'CDXCIX', '499'
#     assert checkio(3789) == 'MMMDCCCLXXXVIII', '3888'
#     print('Done! Go Check!')

#task The Longest Palindromic

# Напишите функцию, которая найдет самый длинный палиндром в строке. Постарайтесь быть максимально эффективными при решении этой задачи.
# Если найдено более одной палиндром с максимальной длинной, то верните тот, который находится ближе к началу строки.

#Сам не решил ( код из инета )

# def longest_palindromic(text):
#     for i in range(len(text)):
#         for j in range(i+1):
#             k = text[j:j+len(text)-i:]
#             if k==k[::-1]:
#                 return k
#
# if __name__ == '__main__':
#     print("Example:")
#
#     assert longest_palindromic('abacada') == 'aba'
#     assert longest_palindromic('babl') == 'AZAZA'
#     assert longest_palindromic('aaaaa') == 'aaaaa'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Numbers Factory

# Дано число N. Необходимо найти наименьшее положительное целое число X,
# такое, что произведение его цифр будет равна N. Если X не существует - верните 0.
# Рассмотрим пример. N = 20. Мы можем разложить данное число, как 2*10, но 10 - это не цифра.
# Также можно разложить N, как 4*5 или 2*2*5. Наименьшее число для 2*2*5 - это 225, для 4*5 -45. Результат 45.

#Сам не сделал код с инета

# def checkio(data):
#     fs = []
#     for p in range(9, 1, -1):
#         while bool(data) and ((data % p) == 0):
#             fs.append(str(p))
#             data /= p
#     return int(''.join(sorted(fs))) if data == 1 else 0
#
# if __name__ == '__main__':
#     # #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert checkio(125) == 45, "1st example"
#     assert checkio(3402) == 37, "2nd example"
#     # assert checkio(17) == 0, "3rd example"
#     # assert checkio(33) == 0, "4th example"
#     assert checkio(3125) == 55555, "5th example"
#     assert checkio(9973) == 0, "6th example"

#task Largest Rectangle in a Histogram

# У вас есть гистограмма. Попробуйте найти размер самого большого прямоугольника, который можно построить из столбцов гистограммы.

#Сам не сделал код с инета

# def largest_histogram(h):
#     result = min(h) * len(h)
#     for w in range(1, len(h)):
#         for i in range(len(h) - w + 1):
#             result = max(result, min(h[i:i + w]) * w)
#     return result
#
# if __name__ == "__main__":
#     assert largest_histogram([5]) == 5, "one is always the biggest"
#     assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
#     assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
#     assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
#     assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"

#task Long Repeat Inside

# Вам необходимо разыскать повторяющуюся последовательность в подстроке. У меня есть небольшой пример: в строке "abababc" - "ab" является
# последовательностью, которая повторяется более одного раза, поэтому ответом будет "ababab".

#my code

# from itertools import groupby
#
# def repeat_inside(line):
#     List = []
#     for i in range(len(line)):
#         for j in range(i + 1):
#             List.append(line[j : j + len(line) - i:])
#     groups = []
#     uniquekeys = []
#     for k, g in groupby(List):
#         groups.append(tuple(g))
#         uniquekeys.append(k)
#     for h in uniquekeys:
#         if line.count(h) > 1:
#             re = h * line.count(h)
#             if re not in line:
#                 re = re[len(h)::]
#             if re + re[0] == line:
#                 re = (re + re[0])
#                 return re
#             return re
#     return ""

#code from internet

# import re

# Regex from the outside in:
# Outer (?=...) lookahead to capture potentially overlapping matches
# Next (...) to capture whole match as group 1
# Inner (...)\2+ to match group 2, followed by itself one or more times
# .+? the unit that gets repeated.  + to ensure at least one character,
# non-greedy +? so that 'aaaaa' will match as five repetitions of 'a'
# instead of as two repetitions of 'aa'.

# def repeat_inside(line):
#     matches = re.findall(r'(?=((.+?)\2+))', line)
#     return max((m[0] for m in matches), key=len, default='')

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert repeat_inside('aaaaa') == 'aaaaa', "First"
#     assert repeat_inside('aabbff') == 'aa', "Second"
#     assert repeat_inside('aababcc') == 'abab', "Third"
#     assert repeat_inside('abc') == '', "Forth"
#     assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
#     print('"Run" is good. How is "Check"?')

#task Reverse Roman Numerals

# Вам предоставляется римское число в виде строки.
# Ваша задача заключается в том, чтобы преобразовать это число в ее десятичное представление.

# def reverse_roman(roman_string):
#
#     Dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "I": 1,
#             "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     Number = 0
#     for key in Dict.keys():
#         Number += Dict[key] * roman_string.count(key)
#         roman_string = roman_string.replace(key, "")
#     return Number
#
#
# if __name__ == '__main__':
#     # assert reverse_roman('VI') == 6, '6'
#     # assert reverse_roman('LXXVI') == 76, '76'
#     assert reverse_roman('CDXCIX') == 499, '499'
#     # assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'

#task Date and Time Converter

# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.

# def date_time(time: str) -> str:
#     dict = {1 : "January", 2 : " February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July",
#             8: "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
#
#     return str(int(time[0:2])) + " " + dict[int(time[3:5])] + " " + time[6:10] \
#     + " year " + str(int(time[11:13])) + (" hour " if int(time[11:13]) == 1 else " hours ") \
#     + str(int(time[14:16])) + (" minute" if int(time[14:16]) == 1 else " minutes")

#code from answer

# from datetime import datetime
#
# def date_time(time):
#     t = datetime.strptime(time, '%d.%m.%Y %H:%M')
#     y, m, d, h, mi = t.year, datetime.strftime(t, '%B'), t.day, t.hour, t.minute
#     suffix = lambda n: 's' if n != 1 else ''
#
#     return f'{d} {m} {y} year {h} hour{suffix(h)} {mi} minute{suffix(mi)}'

# if __name__ == '__main__':
#     print("Example:")
#     # print(date_time('01.01.2000 00:00'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
#     assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
#     assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Army Battles

# В прошлой миссии — Warriors — вы научились устраивать дуэли между 2 отдельными воинами. Отличная работа!
# Но давайте перейдём к чему-то более эпичному — к армиям!
# В этой миссии ваша задача — добавить к уже существующим классам и функциям новые: Army,
# который будет обладать методом add_units(), позволяющим добавлять выбранное количество воинов в армию,
# а также класс Battle() с функцией fight(), которая будет устраивать сражения и определять сильнейшую армию.
# Сражения между армиями происходят по следующему принципу:
# • сперва проводится дуэль между первым воином первой армии и первым воином второй
# • как только один из них погибает — в дуэль вступает следующий воин из той армии, которая потеряла бойца,
# а выживший воин со своим текущим здоровьем продолжает сражаться
# • так продолжается до тех пор, пока все воины одной из армий не умрут. В этом случае функция battle() возвращает True,
# если первая армия выиграла или False, если вторая оказалась сильнее.

# Taken from mission The Warriors

# class Army:
#     def __init__(self):
#         self.army = []
#
#     def add_units(self, Unit, Count):
#         self.army += [Unit() for i in range(Count)]
#
#     @property
#     def is_alive(self):
#         return self.army != []
#
# class Battle:
#     def fight(self, Army1, Army2):
#         while Army1.is_alive and Army2.is_alive:
#             if fight(Army1.army[0], Army2.army[0]):
#                 Army2.army.pop(0)
#             else:
#                 Army1.army.pop(0)
#         return Army1.is_alive
#
# class Warrior:
#     health = 50
#     attack = 5
#
#     @property
#     def is_alive(Warrior):
#         return Warrior.health > 0
#
# class Knight(Warrior):
#     attack = 7
#     pass
#
# def fight(unit_1, unit_2):
#     while True:
#         unit_2.health -= unit_1.attack
#         if not unit_2.is_alive:
#             break
#         unit_1.health -= unit_2.attack
#         if not unit_1.is_alive:
#             break
#     return True if unit_1.is_alive else False
#
# if __name__ == '__main__':
#
#     chuck = Warrior()
#     bruce = Warrior()
#     carl = Knight()
#     dave = Warrior()
#     mark = Warrior()
#
#     assert fight(chuck, bruce) == True
#     assert fight(dave, carl) == False
#     assert chuck.is_alive == True
#     assert bruce.is_alive == False
#     assert carl.is_alive == True
#     assert dave.is_alive == False
#     assert fight(carl, mark) == False
#     assert carl.is_alive == False
#
# if __name__ == '__main__':
#     # fight tests
#     chuck = Warrior()
#     bruce = Warrior()
#     carl = Knight()
#     dave = Warrior()
#     mark = Warrior()
#
#     assert fight(chuck, bruce) == True
#     assert fight(dave, carl) == False
#     assert chuck.is_alive == True
#     assert bruce.is_alive == False
#     assert carl.is_alive == True
#     assert dave.is_alive == False
#     assert fight(carl, mark) == False
#     assert carl.is_alive == False
#
#     # battle tests
#     my_army = Army()
#     my_army.add_units(Knight, 3)
#
#     enemy_army = Army()
#     enemy_army.add_units(Warrior, 3)
#
#     army_3 = Army()
#     army_3.add_units(Warrior, 20)
#     army_3.add_units(Knight, 5)
#
#     army_4 = Army()
#     army_4.add_units(Warrior, 30)
#
#     battle = Battle()
#
#     assert battle.fight(my_army, enemy_army) == True
#     assert battle.fight(army_3, army_4) == False
#     print("Coding complete? Let's try tests!")
