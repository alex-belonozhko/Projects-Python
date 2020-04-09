def funk (x):
    def add (a):
        return x + a
    return add

test = funk (100)
print (test (200))

#test =  def add (a):
#            return 100 + a

add = lambda x, y: x + y

print (add (2, 4))

def K (*Kortezh):
    return Kortezh

def D (**Dictionary):
    return Dictionary

print (K (1, 3, 7, 4))
print (D (A="1", B="2"))





