# 4. have parameter have return
def sum_number (n1, n2, n3) :
    total = n1 + n2 + n3
    return total

def welcome (name) :
    message = 'Hello ' + name
    return message

print(sum_number(1, 2, 3))
print(welcome('Pong'))
print(sum_number(10, 20, 30))

data1, data2 = welcome('Mod')
print(data1)
print(data2)