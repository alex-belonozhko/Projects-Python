#task Pearls in the Box

# Дана информация о начальном наборе жемчужин, как строка из "b" (черная) и "w" (белая) и количество итераций (N). Порядок жемчужин не важен.
# Output: Вероятность вытащить белую жемчужину, как число (float).

# def checkio(marbles: str, step: int) -> float:
#     List = []
#     ReserveList = []
#     if marbles.count("w") == len(marbles) or marbles.count("b") == len(marbles):
#         List.append([1, marbles])
#         n = 2
#     else:
#         List.append([marbles.count("w") / len(marbles), (marbles.count("w") - 1) * "w" + (marbles.count("b") + 1) * "b"])
#         List.append([marbles.count("b") / len(marbles), (marbles.count("b") - 1) * "b" + (marbles.count("w") + 1) * "w"])
#         n = 1
#     for i in range(3, step + n):
#         for j in List:
#             if j[1].count("w") == len(j[1]):
#                 ReserveList.append([j[0] * j[1].count("w") / len(j[1]), (j[1].count("w") - 1) * "w" + "b"])
#             elif j[1].count("b") == len(j[1]):
#                 ReserveList.append([j[0] * j[1].count("b") / len(j[1]), (j[1].count("b") - 1) * "b" + "w"])
#             else:
#                 ReserveList.append([j[0] * j[1].count("w") / len(j[1]), (j[1].count("w") - 1) * "w" + (j[1].count("b") + 1) * "b"])
#                 ReserveList.append([j[0] * j[1].count("b") / len(j[1]), (j[1].count("b") - 1) * "b" + (j[1].count("w") + 1) * "w"])
#         List = [h for h in ReserveList if h[0] != 0]
#         ReserveList = []
#     Answer = 0
#     for k in List:
#         Answer += k[0] * (k[1].count("w") / len(k[1]))
#     return round(Answer, 2)

#task Skew-symmetric Matrix

# Вы должны определить, является ли указанная квадратная матрица кососимметричной или нет.

#my code ( tazasho? )

# def funk(matrix, Index, IndexBreak):
#     TestList = []
#     for j in matrix:
#         TestList.append(j[Index])
#         if IndexBreak == 0:
#             if len(TestList) % 2 != 0:
#                 del TestList[int(len(TestList) / 2)]
#             Test1 = TestList[0:int(len(TestList) / 2)]
#             Test2 = TestList[:int(len(TestList) / 2) - 1:-1]
#             for test1symbol, test2symbol in zip(Test1, Test2):
#                 if test1symbol != test2symbol * -1:
#                     return False
#             return True
#         IndexBreak -= 1
#         Index -= 1
#
# def checkio(matrix):
#     if len(matrix) == 1 and matrix[0][0] == 0:
#         return True
#     Index = 0
#     for i in matrix:
#         if i[Index] != 0:
#             return False
#         Index += 1
#     Index = 1
#     IndexBreak = 1
#     while True:
#         if funk(matrix, Index, IndexBreak) == False:
#             return False
#         elif len(matrix) == 2:
#             return True
#         if IndexBreak == len(matrix) - 1:
#             del matrix[0]
#             IndexBreak -= 1
#         else:
#             Index += 1
#             IndexBreak += 1

# XXXXDDDDD
# def checkio(matrix):
#     return matrix == [[-x for x in row] for row in zip(*matrix)]

# if __name__ == '__main__':
#     assert checkio([
#         [0, 1, 2],
#         [-1, 0, 1],
#         [-2, -1, 0]]) == True, "1st example"
#     assert checkio([
#         [0, 1, 2],
#         [-1, 1, 1],
#         [-2, -1, 0]]) == False, "2nd example"
#     assert checkio([
#         [0, 1, 2],
#         [-1, 0, 1],
#         [-3, -1, 0]]) == False, "3rd example"

#task Broken Clock

# Даны три значения. Первое - это изначальное время, когда установили часы правильно.
# Второе - время в текущий момент на часах (неверное конечно).
# Время записанов в формате "чч:мм:сс" (например: "01:16:59" и "23:00:13").
# Третье значение - это описание ошибки часов Для пример "+1 second at 10 seconds"

# from datetime import datetime
#
# def broken_clock(starting_time, wrong_time, error_description):
#     DictTime = {"second" : 1, "seconds" : 1, "minute" : 60, "minutes" : 60, "hour" : 3600, "hours" : 3600}
#     WT, ST = datetime.strptime(wrong_time, '%H:%M:%S'), datetime.strptime(starting_time, '%H:%M:%S')
#     Et, Etd, _, Ea, Ead = error_description.split()
#     ErrorTime = int(Et) * DictTime[Etd]
#     ErrorAt = int(Ea) * DictTime[Ead]
#     return (ST + (WT - ST) * ErrorAt / (ErrorTime + ErrorAt)).strftime('%X')
#
# if __name__ == "__main__":
#     assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
#     assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
#     assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
#     assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
#     assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'

#task Achilles and the Tortoise

# Даны скорости A1 и T2 в м/с, а ткаже преимущество T2 в секундах. Подсчитайте время,
# когда A1 поровняется с T2 (считая от времени старта T2). Результат должен быть с точностью до 8 знаков.

#my code ( решает задачу правильно но задачу нужно было решить не правильно )

# from itertools import count
#
# def chase(a1_speed, t2_speed, advantage):
#     t2distance = t2_speed * advantage
#     a1distance = 0
#     for i in count(3):
#         t2distance += t2_speed
#         a1distance += a1_speed
#         if a1distance == t2distance:
#             re = i
#             return i
#         elif a1distance > t2distance:
#             excessDistance = a1distance % t2distance
#             meetDistance = a1_speed - excessDistance
#             timeMeetDistance = meetDistance / a1_speed
#             anwer = round((i - 1) + timeMeetDistance, 8)
#             return anwer

# true code ( trash )
# def chase(a1_speed, t2_speed, advantage):
#     return (t2_speed * advantage) / (a1_speed - t2_speed) +  advantage

# if __name__ == '__main__':
#     def almost_equal(checked, correct, significant_digits):
#         precision = 0.1 ** significant_digits
#         return correct - precision < checked < correct + precision
#
#     # assert almost_equal(chase(6, 3, 2), 4, 8), "example"
#     assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"

#task Cut Sentence

# В этой миссии Ваша задача состоит в том, чтобы урезать предложение до длины, которая не превышает заданное количество символов.

# def cut_sentence(line, length):
#     TrueLine = line[:length].split()
#     OldLine = line.split()
#     if TrueLine == OldLine:
#         return ' '.join(TrueLine)
#     for first, second in zip(TrueLine, OldLine):
#         if first != second:
#             TrueLine.pop()
#     return ' '.join(TrueLine) + "..."

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
#     # assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
#     assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
#     assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
#     print('Done! Do you like it? Go Check it!')

#task Binary Count

# Дано положительное целое число.
# Вам необходимо сконвертировать его в двоичную форму и подсчитать сколько единиц в написании данного числа.

# checkio = lambda number: bin(number).count("1")
#
# if __name__ == '__main__':
#     assert checkio(4) == 1
#     assert checkio(15) == 4
#     assert checkio(1) == 1
#     assert checkio(1022) == 9
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#task Caesar Cipher (decryptor)

# Например, ("a b c", 3) == "d e f" Также вам нужно будет игнорировать/удалить все специальные символы

# def to_decrypt(cryptotext, delta):
#     for i in cryptotext:
#         if not i.isalpha() and i != " ":
#             cryptotext = cryptotext[:cryptotext.index(i)] + cryptotext[cryptotext.index(i) + 1:]
#     cryptotext = list(cryptotext)
#     for j in range(len(cryptotext)):
#         if cryptotext[j].isalpha():
#             TrueChar = ord(cryptotext[j]) + delta
#             if TrueChar < 97:
#                 TrueChar = 122 - (97 - TrueChar - 1)
#             elif TrueChar > 122:
#                 TrueChar = 97 + (TrueChar - 122 - 1)
#             cryptotext[j] = chr(TrueChar)
#     return ''.join(cryptotext)

# if __name__ == '__main__':
    # assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    # assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    # assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    # assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    # assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    # print("Coding complete? Click 'Check' to earn cool rewards!")