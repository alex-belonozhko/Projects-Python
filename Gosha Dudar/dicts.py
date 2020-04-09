# Gosha Dudar method create dictionary
d = {'Alex' : "19", 'Renat' : "21"}
d['Alex'] = 21
# print (d['Alex'])

# Second method create dictionary
d = dict(short="Alex", long="Alexey")
d['short'] = "Al"
# print(d["short"])

# Third method create dictionary
d = dict.fromkeys(['Alex', 'Alexey', 'Al'], 19)
d['Al'] = 21
# print (d)

# Fourth method create dictionary
d = {age : age ** 2  for age in range(5)}
# print (d)

# Example
partner = {'Name' : {'name' : "Alex", 'surname' : "Ivanov", 'patronymic' : "Olegovich"},
           'Contacts' : {'home number' : "38 993", 'mobile number' : "3 8 097 06 16 134"},
           'residence' : ["c.Boyarka s.Lomonosova 54"]}
print (partner['Name']['surname'])
print (partner['Name']['name'])
print (partner['Name']['patronymic'])

