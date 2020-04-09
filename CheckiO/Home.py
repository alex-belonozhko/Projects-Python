#task All the Same

# In this mission you should check if all elements in the given list are equal.
# Input: List.
# Output: Bool.
# The idea for this mission was found on Python Tricks series by Dan Bader
# Precondition: all elements of the input list are hashable

# from typing import List, Any
#
# def all_the_same(elements: List[Any]) -> bool:
#     if len(elements) != 0:
#         if len(set(elements)) == 1:
#             return True
#         else:
#             return False
#     else:
#         return True
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([1, 2, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task House Password

# Stephan and Sophia forget about security and use simple passwords for everything.
# Help Nikola develop a password security check module. The password will be considered strong enough
# if its length is greater than or equal to 10 symbols,
# it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
# The password contains only ASCII latin letters or digits.
# Input: A password as a string.
# Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
# In the results you will see the converted results.

# def checkio(data: str) -> bool:
#     g = 0
#     d = 0
#     f = 0
#     if len(data) < 10:
#         return False
#     for i in data:
#         if i.isupper():
#             g += 1
#         elif i.islower():
#             d += 1
#         elif i.isdigit():
#             f += 1
#     if g > 0 and d > 0 and f > 0:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#task The Most Wanted Letter

# You are given a text, which contains different english letters and punctuation symbols.
# You should find the most frequent letter in the text.
# The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,
# "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# Input: A text for analysis as a string.
# Output: The most frequent letter in lower case as a string.
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105

# from collections import Counter
#
# def checkio(text: str) -> str:
#     list = []
#     a_set = set()
#     for Symbol in text:
#         if Symbol.islower() or Symbol.isupper():
#             if Symbol.isupper():
#                 Symbol = Symbol.lower()
#                 a_set.add(Symbol)
#                 list.append(Symbol)
#             else:
#                 a_set.add(Symbol)
#                 list.append(Symbol)
#     a = Counter(list)
#     most_common = None
#     MostCommon = a.most_common()[0][0]
#     CountMostCommon = list.count(MostCommon)
#     ListMostCommon = []
#     for item in a_set:
#         Count = list.count(item)
#         if Count == CountMostCommon:
#             ListMostCommon.append(item)
#     ListMostCommon.sort()
#     return ListMostCommon[0]
#
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio("Hello World!"))
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert checkio("AAaooo!!!!") == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#     print("The local tests are done.")

#task Time Converter (24h to 12h)

# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere.
# # Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# # - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# # - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# # Here you can find some useful information about the 12-hour format.
# # Input: Time in a 24-hour format (as a string).
# # Output: Time in a 12-hour format (as a string).
# # Precondition:
# # '00:00' <= time <= '23:59'

# def time_converter(time):
#     hours, minutes = int(time.split(':')[0]), time.split(':')[1]
#     if hours >=12:
#         if hours >12:
#             hours -= 12
#         time = "{}:{} p.m.".format(hours,minutes)
#     else:
#         if hours == 0:
#             hours += 12
#         time = "{}:{} a.m.".format(hours,minutes)
#     return time
#
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter('23:30'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert time_converter('13:07') == '1:07 p.m.'
#     assert time_converter('09:00') == '9:00 a.m.'
#     assert time_converter('00:01') == '12:01 p.m.'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Non-unique Elements

# You are given a non-empty list of integers (X).
# For this task, you should return a list consisting of only the non-unique elements in this list.
# To do so you will need to remove all unique elements (elements which are contained in a given list only once).
# When solving this task, do not change the order of the list.
# Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

# def checkio(data: list) -> list:
#     ListNonUnique = []
#     for num in data:
#         if data.count(num) > 1:
#             ListNonUnique.append(num)
#     return ListNonUnique
#
# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")

#task Sort Array by Element Frequency

# Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
# the number of times they appear in elements. If two elements have the same frequency,
# they should end up in the same order as the first appearance in the iterable.
# Input: Iterable
# Output: Iterable

# My code

# import collections
#
# def frequency_sort(items):
#     counts = collections.Counter(items)
#     ListFrequency = []
#     for symbol in counts.most_common():
#         CountFrequency = items.count(symbol[0])
#         while CountFrequency != 0:
#             ListFrequency.append(symbol[0])
#             CountFrequency -= 1
#     return ListFrequency

# 1 string )))
# Description:
# Input - frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])
# After applying the key: (-4,0),(-2,1),(-2,2),(-2,2),(-2,1),(-4,0),(-4,0),(-4,0)
# Output: [4, 4, 4, 4, 6, 6, 2, 2]
#
# def frequency_sort(items):
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 6, 2, 2, 4, 4, 4, 2]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Flatten a List

# def flat_list(array):
#     array = str(array).replace('[', '').replace(']', '').replace(',', '').strip()
#     return list(map(int, array.split(' '))) if array else []

# if __name__ == '__main__':
#     assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
#     assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
#     assert flat_list([]) == [], "Third"
#     assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
#     print('Done! Check it')

#task Long Repeat

# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter.
# For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
# The last substring is the longest one, which makes it the answer.

# My code ( bad )

# def long_repeat(line: str) -> int:
#     if line:
#         Answer = 0
#         LongestRepeat = 1
#         PreviousSumbol = None
#         for Symbol in line:
#             if Symbol != PreviousSumbol:
#                 LongestRepeat = 1
#             if Symbol == PreviousSumbol:
#                 if LongestRepeat > Answer:
#                     Answer = LongestRepeat
#                 LongestRepeat += 1
#             PreviousSumbol = Symbol
#         return Answer + 1
#     elif None:
#         return None
#     else:
#         return 0

# answer code ( 1 line)))) )
# groupy делит наш список или стринг на групы которые должныы состоять из одинаковых символов , если символ другой - создаеться новая группа
# from itertools import groupby
#
# def long_repeat(line):
#     return max([len(list(g)) for k, g in groupby(line)], default=0)
#
# # g = [[s], [ddd], [ffff], [ee], [f]] ... выводим длинну максимального списка в g
# # k = [s, d, f, e, f]
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert long_repeat('sdddffffeef') == 4, "First"
#     assert long_repeat('ddvvrwwwrggg') == 3, "Second"
#     assert long_repeat('abababaab') == 2, "Third"
#     assert long_repeat('') == 0, "Empty"
#     print('"Run" is good. How is "Check"?')


#task Sun Angle

# Your task is to find the angle of the sun above the horizon knowing the time of the day.
# Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith,
# which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees.
# If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
# your function should return - "I don't see the sun!"
# 1m = 0.25

# My code

# def sun_angle(time):
#     Hour, Minute = map(int, time.split(':'))
#     if 6 <= Hour <= 18:
#         if Hour == 18 and Minute != 0:
#             return "I don't see the sun!"
#         return (Hour - 6) * 15 + (Minute * 0.25)
#     else:
#         return "I don't see the sun!"

# Perfect code

# def sun_angle(time):
#     h, m = map(int, time.split(':'))
#     angle = 15 * h + m / 4 - 90
#     return angle if 0 <= angle <= 180 else "I don't see the sun!"

# if __name__ == '__main__':
#     print("Example:")
#     # print(sun_angle("16:00"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert sun_angle("14:02") == "I don't see the sun!"
#     assert sun_angle("12:30") == 97.5
#     assert sun_angle("01:23") == "I don't see the sun!"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# task Bird Language

# My code

# VOWELS = "aeiouy"
#
# def translate(phrase):
#     List = list(map(str, phrase))
#     ListAnswer = []
#     c = 0
#     while c < len(phrase):
#         ListAnswer.append(List[c])
#         if List[c] in VOWELS:
#             c += 3
#         elif List[c] == " ":
#             c += 1
#         else:
#             c += 2
#     return ''.join(ListAnswer)

# Code from internet

# VOWELS = "aeiouy"
#
# def translate(phrase):
#     output = ""
#     c = 0
#
#     while c < len(phrase):
#         output += phrase[c]
#         if phrase[c] in VOWELS:
#             c = c + 3
#         elif phrase[c] == ' ':
#             c = c + 1
#         else:
#             c = c + 2
#
#     return output

# if __name__ == '__main__':
#     print("Example:")
#     print(translate("hieeelalaooo"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert translate("hieeelalaooo") == "hello", "Hi!"
#     assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
#     assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
#     assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# task Pawn Brotherhood

# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
# With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
# We have several white pawns on the chess board and only white pawns.
# You should design your code to find how many pawns are safe.
# Кароче нужно сказать за какие пешки отомстят другие печшки в случае побития

#My code

# def safe_pawns(pawns: set) -> int:
#     StrChessBoard = "a8 b8 c8 d8 e8 f8 g8 h8 a7 b7 c7 d7 e7 f7 g7 h7 a6 b6 c6 d6 e6 f6 g6 h6 " \
#                     "a5 b5 c5 d5 e5 f5 g5 h5 a4 b4 c4 d4 e4 f4 g4 h4 a3 b3 c3 d3 e3 f3 g3 h3 " \
#                     "a2 b2 c2 d2 e2 f2 g2 h2 a1 b1 c1 d1 e1 f1 g1 h1"
#     ListChessBoard = list(map(str, StrChessBoard.split(" ")))
#     ListClearBox = []
#     for i in pawns:
#         Index = ListChessBoard.index(i)
#         if 0 <= Index <= 8:
#             continue
#         else:
#             if i[0] == "a":
#                 ListClearBox.append(ListChessBoard[Index - 7])
#             elif i[0] == "h":
#                 ListClearBox.append(ListChessBoard[Index - 9])
#             else:
#                 ListClearBox.append(ListChessBoard[Index - 9])
#                 ListClearBox.append(ListChessBoard[Index - 7])
#     Answer = 0
#     for i in pawns:
#         if i in ListClearBox:
#             Answer += 1
#     return Answer

# Code from genious

# def safe_pawns(pawns):
#     answer = 0
#     for pawn in pawns :
#         if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
#     return answer
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# task Xs and Os Referee

# from typing import List
#
# def checkio(game_result: List[str]) -> str:
#
#     sample = "".join(game_result)
#     data = game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]
#
#     if "OOO" in data:
#         return "O"
#     elif "XXX" in data:
#         return "X"
#     else:
#         return "D"
#
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio(["X.O",
#                    "XX.",
#                    "XOO"]))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio([
#         "X.O",
#         "XX.",
#         "XOO"]) == "X", "Xs wins"
#     assert checkio([
#         "OO.",
#         "XOX",
#         "XOX"]) == "O", "Os wins"
#     assert checkio([
#         "OOX",
#         "XXO",
#         "OXX"]) == "D", "Draw"
#     assert checkio([
#         "O.X",
#         "XX.",
#         "XOO"]) == "X", "Xs wins again"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#task The Warriors

# Начнем с простой задачи - дуэли один на один. Вам необходимо создать класс Warrior,
# экземпляры которого будут иметь 2 параметра - здоровье (равно 50 баллам)
# и атака (равно 5 баллам), а также 1 свойство - is_alive, которое может быть True (если здоровье воина> 0 )
# или Ложь (в другом случае). Кроме того, вы должны создать второй тип юнита - Рыцарь, который должен быть подклассом Воина,
# но иметь увеличенную атаку - 7. Также вы должны создать функцию fight (), которая будет инициировать
# дуэль между 2 воинами и определять самый сильный из них. Поединок происходит по следующему принципу:
# Каждый ход первый воин наносит удар второму, и эта секунда теряет свое здоровье в том же значении, что и атака первого воина.
# После этого, если он еще жив, второй воин сделает то же самое с первым.
# Борьба заканчивается смертью одного из них. Если первый воин все еще жив (и, следовательно, другой больше не существует),
# функция должна вернуть True, False в противном случае.

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
#            break
#         unit_1.health -= unit_2.attack
#         if not unit_1.is_alive:
#            break
#     return unit_1.is_alive
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
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
#     print("Coding complete? Let's try tests!")

# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

# Your optional code here
# You can import some modules or create additional functions


# def best_stock(dict):
#     MaxStock = max(list(map(float, dict.values())))
#     for stock in dict:
#         if dict[stock] == MaxStock:
#             return stock


