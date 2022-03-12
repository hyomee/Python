num01 = 10

def func():
    num01 = 20
    num02 = 10

func()
print(num01)
# UnboundLocalError: local variable 'num01' referenced before assignment
# print( num02)

