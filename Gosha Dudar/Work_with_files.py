t = open ("Lol.txt", "r")
print (t.read ())
t.close ()
t = open ("Lol.txt", "w")
t.write ("Hello!! all")
t.close()
t = open ("Lol.txt", "r")
print (t.read ())
t.close()

#With and as allow automatically close file in case Error

with open('test.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write (line)


