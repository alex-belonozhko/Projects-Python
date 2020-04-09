#Example 1
# class car:
#     color = "color"
#     engine = "engine"
#     weight = "weight"
#
#     def set(self, color, engine, weight):
#         self.color = color
#         self.engine = engine
#         self.weight = weight
#
# class Mark (car):
#     mark = "mark"
#
#     def __init__(self, mark, weight):
#         self.mark = mark
#         self.weight = weight
#
# class mark (car):
#     mark = "mark"
#
#     def mk(self, mark):
#         self.mark = mark
#
# Sens = Mark("Sens", "2499kg")
# Sens.set("grey", 2, "2500kg")
#
# Audi = mark()
# Audi.mk("Audi")
# Audi.set("white", 3, "3000kg")
#
# BMW = mark()
# BMW.set("black", 4, "3500kg")
# BMW.mk("BMW")
#
# print (BMW  .mark)

#Example 2

# class Car:
#     def __init__(self, mark, engine):
#         self.mark = mark
#         self.engine = engine
#         print("Создан обьект класа Car с параметрами: Марка: {0} и Двигатель: {1}".format(self.mark, self.engine))
#
#     def tell(self):
#         print("Марка: {0}, Двигатель: {1}, ".format(self.mark, self.engine), end=" ")
#
# class Purchase:
#     def __init__(self, mark, engine, profit):
#         Car.__init__(self, mark, engine)
#         self.profit = profit
#         print("Вы продали машину Марки {0} с движком {1} по заработали {2}".format(self.mark, self.engine, self.profit))
#     def tell(self):
#         Car.tell(self)
#         print("Стоимость: {0}".format(self.profit))
#
# class Sale:
#     def __init__(self, mark, engine, cost):
#         Car.__init__(self, mark, engine)
#         self.cost = cost
#         print("Вы купили машину Марки {0} с движком {1} по стоимости {2}".format(self.mark, self.engine, self.cost))
#     def tell(self):
#         Car.tell(self)
#         print("Стоимость: {0}".format(self.cost))
#
# S = Sale("Sens", 2, 2000)
# P = Purchase("BMW", 4, 6000)
# Cars = [S, P]
# for car in Cars:
#     car.tell()
