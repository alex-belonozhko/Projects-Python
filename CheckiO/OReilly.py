#task Median

# В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.

# from typing import List
#
# def checkio(data: List[int]) -> [int, float]:
#     LenData = len(sorted(data))
#     data.sort()
#     half = len(data) // 2
#     return (data[half] + data[~half]) / 2
#
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio([1, 2, 3, 4, 5]))
#
#     assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
#     assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
#     assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
#     assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
#     print("Start the long test")
#     assert checkio(list(range(1000000))) == 499999.5, "Long."
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Days Between

# Посчитать Разницe между датами в днях, как целое число.

# from datetime import datetime
#
# def days_diff(a, b):
#     return abs((datetime(b[0], b[1], b[2]) - datetime(a[0], a[1], a[2])).days)
#
# if __name__ == '__main__':
#     print("Example:")
#     print(days_diff((1982, 4, 19), (1982, 4, 22)))
#
#     assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
#     assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
#     assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task How to Find Friends

# Попробуйте определить, связаны ли они через других дронов

#Сам не смог решить

# def check_connection(network, first, second):
#     team = {first}
#     for _ in network:
#         for edge in network:
#             pair = set(edge.split('-'))
#             if pair & team:
#                 team |= pair
#     return second in team
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert check_connection(
#         ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#          "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#         "scout2", "scout3") == True, "Scout Brotherhood"
#     assert check_connection(
#         ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#          "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#         "super", "scout2") == True, "Super Scout"
#     assert check_connection(
#         ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#          "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#         "dr101", "sscout") == False, "I don't know any scouts."

#task Worth of Words

# Каждое слово имеет ценность, которая эквивалентна сумме очков всех букв, входящих в него.
# Стоимость букв следующая:
# e, a, i, o, n, r, t, l, s, u = 1
# d, g = 2
# b, c, m, p = 3
# f, h, v, w, y = 4
# k = 5
# j, x = 8
# q, z = 10
# Найти  Самое ценное слово

# VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
#           't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
#           'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
#           'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
#           'q': 10, 'z': 10}

#my code

# def worth_of_words(words):
#     MostWorthWord = ""
#     CostMostWorthWord = 0
#     for word in words:
#         Cost = 0
#         for i in word:
#             if i in VALUES:
#                 Cost += VALUES[i]
#         if Cost > CostMostWorthWord:
#             CostMostWorthWord = Cost
#             MostWorthWord = word
#     return MostWorthWord

# one line from answer

# def worth_of_words(words):
#     return max(words, key=lambda w: sum(VALUES[c] for c in w))

# if __name__ == '__main__':
#     print("Example:")
#     print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
#     assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

#task Cipher Map

# Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками.
# Поместите решетку на листе бумаги такого же размера с буквами, выписываете первые 4 символа, которые видно в окошках (см. рисунок).
# Затем поверните решетку на 90 градусов по часовой стрелке. Выпишите следующие символы и повторите поворот.
# В итоге процедура повторяется 4 раза.

#My code

# def CalcPassword(ListIndex, NewListIndex, Password, NewCP, q):
#     List = []
#     if q == 0 or q == 2:
#         for d in range(4):
#             MinNewListIndex = NewListIndex.index(min(NewListIndex))
#             List.append(ListIndex[MinNewListIndex])
#             NewListIndex[MinNewListIndex] = max(NewListIndex) + 1
#         if q == 0:
#             for h in List:
#                 Password += NewCP[h]
#         else:
#             for h in reversed(List):
#                 Password += NewCP[h]
#     else:
#         for h in reversed(ListIndex):
#             Password += NewCP[h]
#     return Password
#
# def recall_password(cipher_grille, ciphered_password):
#     CP, CG = [k for k in ''.join(ciphered_password)], [h for h in ''.join(cipher_grille)]
#     ListIndex = []
#     Answer = ""
#     for j in CG:
#         if j == "X":
#             ListIndex.append(CG.index(j))
#             CG.insert(CG.index(j), "Y")
#             CG.remove("X")
#     for h in ListIndex:
#         Answer += CP[h]
#         indexCP = 3
#         NewIndexCP = indexCP
#         NewCP = []
#         NewListIndex = []
#     for q in range(3):
#         ListIndexIndex = 0
#         for f in range(0, 15+1):
#             if f in ListIndex:
#                 NewListIndex.append(NewIndexCP)
#             NewCP.append(CP[NewIndexCP])
#             NewIndexCP += 4
#             if NewIndexCP > 15:
#                 indexCP -= 1
#                 NewIndexCP = indexCP
#         Answer = CalcPassword(ListIndex, NewListIndex, Answer, NewCP, q)
#         NewListIndex.clear()
#         CP = NewCP[:]
#         NewCP.clear()
#         indexCP = 3
#         NewIndexCP = indexCP
#     return Answer

#code from answer

# def recall_password(grill, cypher):
#     password = ""
#     for _ in grill:  # must be of len 4
#         for grill_row, cypher_row in zip(grill, cypher):
#             for grill_letter, cypher_letter in zip(grill_row, cypher_row):
#                 if grill_letter == 'X':
#                     password += cypher_letter
#         row1, row2, row3, row4 = grill
#         grill = tuple(zip(row4, row3, row2, row1))  # rotate
#     return password

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recall_password(
#         ('X...',
#          '..X.',
#          'X..X',
#          '....'),
#         ('itdf',
#          'gdce',
#          'aton',
#          'qrdi')) == 'icantforgetiddqd', 'First example'
#
#     assert recall_password(
#         ('....',
#          'X..X',
#          '.X..',
#          '...X'),
#         ('xhwc',
#          'rsqx',
#          'xqzz',
#          'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

#task Striped Words

# Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными (полосатые слова),
# то есть в таких словах нет двух гласных или двух согласных букв подряд.

# VOWELS = "AEIOUY"
# CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
# PunctuationMark = (",", "[", "]", ":", ",", "-", "...", \
#                    "!", "_", "(", ")", ".", "?", "'", ";")
#
# def checkio(text):
#     text = text.upper()
#     for f in PunctuationMark:
#          text = text.replace(f, " ")
#     List = []
#     for i in CONSONANTS:
#         text = text.replace(i, "C")
#     for j in VOWELS:
#         text = text.replace(j, "V")
#     text = text.split()
#     for n in text:
#         if ("VV" not in n) and ("CC" not in n) and (len(n) > 1) and (n.isalpha()):
#             List.append(n)
#     return len(List)
#
# if __name__ == '__main__':
#     assert checkio("My name is ...") == 3, "All words are striped"
#     assert checkio("Hello world") == 0, "No one"
#     assert checkio("A quantity of striped words.") == 1, "Only of"
#     assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

#task Feed Pigeons

# Я начал кормить одного из голубей. Через минуту прилетело еще два,
# и еще через минуту прилетело еще три голубя. Затем 4 и так далее (Пр: 1+2+3+4+...).
# Одной порции корма хватает одному голубю на минуту. В случае если еды не хватает на всех птиц, то сначала едят те голуби,
# что прилетели ранее. Голуби - это вечно голодные птицы и они будут есть и есть без остановки. Если у меня есть N порций корма,
# то сколько голубей я смогу покормить хотя бы по разу?

# def checkio(number):
#     pigeons = {}
#     FullPig = 0
#     n = 1
#     while number > sum(pigeons.keys()):
#         for pigeon in pigeons.values():
#             pigeons[pigeon.count("1")] = "0" * pigeon.count("1")
#         pigeons[n] = "0"*n
#         for pigeon in pigeons.values():
#             for i in pigeon:
#                 if number > 0:
#                     if int(pigeons[pigeon.count("0")]) * 1 > 0:
#                         pigeons[pigeon.count("0")] += "1"
#                     else:
#                         pigeons[pigeon.count("0")] = "1"
#                 else:
#                     continue
#                 number -= 1
#             if number <= 0:
#                 FullPig += pigeons[n].count("1")
#                 break
#             FullPig += pigeons[n].count("1")
#         n += 1
#     return FullPig

#code from answer

# """Determine the number of (greedy) pigeons who will be fed."""
# import itertools
#
# def checkio(food):
#     """Given a quantity of food, return the number of pigeons who will eat."""
#     pigeons = 0
#     for t in itertools.count(1):
#         if pigeons + t > food:
#             # The food will be consumed this time step.
#             # All pigeons around last time were fed, and there is enough food
#             # this time step to feed 'food' pigeons, so return the max of each.
#             return max(pigeons, food)
#         # Increase pigeons, decrease food.
#         pigeons += t
#         food -= pigeons
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(3) == 2, "1st example"
#     assert checkio(2) == 1, "2nd example"
#     assert checkio(5) == 3, "3rd example"
#     assert checkio(11) == 6, "4th example"

#task Boolean Algebra

# OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
#
# def boolean(x, y, operation):
#     if operation == "conjunction":
#         return 1 if x == y == 1 else 0
#     elif operation == "disjunction":
#         return 1 if x == 1 or y == 1 else 0
#     elif operation == "implication":
#         return y if x == 1 else 1
#     elif operation == "exclusive":
#         return 1 if x != y else 0
#     elif operation == "equivalence":
#         return 1 if x == y else 0
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert boolean(1, 1, "conjunction") == 0, "and"
#     assert boolean(1, 0, "disjunction") == 1, "or"
#     assert boolean(0, 0, "implication") == 1, "material"
#     assert boolean(0, 1, "exclusive") == 1, "xor"
#     assert boolean(0, 1, "equivalence") == 0, "same?"
#     print('All good! Go and check the mission.')

#task Ghosts Age

# 1 год -- 10000 - 1 = 9999 (1 число Фибоначчи).
# 2 года -- 9999 - 2 = 9997 (2 число Фибоначчи).

#my code

# from itertools import count
#
# def checkio(opacity):
#     Pred = 2
#     PredPred = 1
#     FibonachiList = [1, 2]
#     while FibonachiList[-1] <= 10000:
#         FibonachiList.append(Pred + PredPred)
#         PredPred, Pred = Pred, Pred + PredPred
#     MaxOpacity = 10000
#     for i in count(0):
#         if MaxOpacity == opacity:
#             return i
#         if i + 1 in FibonachiList or i == 0:
#             MaxOpacity -= FibonachiList[0]
#             del FibonachiList[0]
#         else:
#             MaxOpacity += 1

# if __name__ == '__main__':
    # assert checkio(10000) == 0, "Newborn"
    # assert checkio(9999) == 1, "1 year"
    # assert checkio(9997) == 2, "2 years"
    # assert checkio(9994) == 3, "3 years"
    # assert checkio(9995) == 4, "4 years"
    # assert checkio(9990) == 5, "5 years"

#task Friends

# class Friends:
#     def __init__(self, connections):
#         self.connections = list(connections)
#
#     def add(self, connection):
#         if connection not in self.connections:
#             self.connections.append(connection)
#             return True
#         else:
#             return False
#
#     def remove(self, connection):
#         if connection in self.connections:
#             self.connections.remove(connection)
#             return True
#         else:
#             return False
#
#     def names(self):
#         List = []
#         for i in self.connections:
#             for j in i:
#                 if j not in List:
#                     List.append(j)
#         return set(List)
#
#     def connected(self, name):
#         t = False
#         for a in self.connections:
#             if name in a:
#                 t = True
#         if t == True:
#             team = set()
#             for g in self.connections:
#                 if name in g:
#                     team |= g
#             List = list(team)
#             List.remove(name)
#             return set(List)
#         else:
#             return set()

# if __name__ == '__main__':
#
#     letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
#     digit_friends = Friends([{"1", "2"}, {"3", "1"}])
#     assert letter_friends.add({"c", "d"}) is True, "Add"
#     assert letter_friends.add({"c", "d"}) is False, "Add again"
#     assert letter_friends.remove({"c", "d"}) is True, "Remove"
#     assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
#     assert letter_friends.names() == {"a", "b", "c"}, "Names"
#     assert letter_friends.connected("d") == set(), "Non connected name"
#     assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

#task Create Intervals

# Значения могут быть в одном интервале только если разность между значением и следующим меньшим значением в наборе равно единице,
# иначе начинается новый интервал.

# def create_intervals(data):
#     ListData = sorted(list(data))
#     List = []
#     TestList = []
#     Num = None
#     for i in ListData:
#         if Num == None:
#             Num = i
#             TestList.append(i)
#         elif i - TestList[-1] == 1:
#             TestList.append(i)
#         elif i - TestList[-1] == -1:
#             TestList.insert(TestList.index(TestList[-1]), i)
#         elif i - Num != 1:
#             List.append(TestList[:])
#             TestList.clear()
#             TestList.append(i)
#     List.append(TestList[:])
#     TestList.clear()
#     for k in List:
#         if k:
#             TestList += [tuple([k[0], k[-1]])]
#         else:
#             break
#     return TestList

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
#     assert create_intervals({8,9,6,7}) == [(1, 8)], "Second"
#
#     print('Almost done! The only thing left to do is to Check it!')

#task Long Non Repeat

# Здесь Вам необходимо найти первую самую длинную подстроку состоящую исключительно из неповторяющихся букв. Например,
# в строке "abca" мы имеем две подстроки с неповторяющимися буквами "abc" и "bca",
# но нам нужна первая подстрока, поэтому ответом будет "abc".

# def funk(line):
#     Str = ""
#     for j in line:
#         if j not in Str:
#             Str += j
#         else:
#             return Str
#     return Str
#
# def non_repeat(line):
#     if not line:
#         return ""
#     List = []
#     while line:
#         List.append(funk(line))
#         line = line[1::]
#     return sorted(List, key = len, reverse = True)[0]

# if __name__ == '__main__':
#
#     assert non_repeat('abdjwawk') == 'abdjw', "First"
#     assert non_repeat('abdjwawk') == 'abdjw', "Second"
#     assert non_repeat('abcabcffab') == 'abcf', "Third"
#     print('"Run" is good. How is "Check"?')

#task Text Editor

# В этой миссии вы поможете этим людям, создав прототип текстового редактора с возможностью сохранять различные версии текста,
# а затем возвращаться к любой из них.

# class Text:
#     text = ""
#     font = ""
#     def write(self, text):
#         self.text += text
#
#     def set_font(self, font):
#         self.font += f'[{font}]'
#
#     def show(self):
#         return self.font + self.text + self.font
#
#     def restore(self, DictElement):
#         self.text, self.font = DictElement
#
# class SavedText:
#     Dict = {}
#     def save_text(self, text):
#         self.Dict[len(self.Dict)] = [text.text, text.font]
#
#     def get_version(self, number):
#         return self.Dict[number]
#
# if __name__ == '__main__':
#     text_2 = Text()
#     saver_2 = SavedText()
#     text_2.write("Tomorrow at 7:15 PM.")
#     saver_2.save_text(text_2)
#     text_2.set_font("ComicSans")
#     text_2.write(" Sorry. 7:15 AM.")
#     saver_2.save_text(text_2)
#     text_2.write(" Near the stadium.")
#     text_2.restore(saver_2.get_version(0))
#     print(text_2.show())
#     print("Coding complete? Let's try tests!")

#task Remove Accents

#Ничего не понятно

# from unicodedata import normalize, category
#
# def checkio(in_string):
#     return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')
#
# if __name__ == '__main__':
#     assert checkio(u"完好無缺") == u"完好無缺"
#     assert checkio(u"loài trăn lớn") == u"loai tran lon"
#     print('Done')
