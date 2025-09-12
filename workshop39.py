def show_program_name( ) :
    print('--------------------')
    print(' โปรแกรมคูณเลข ')
    print('--------------------')

def input_number1() :
    print('ป้อนตัวเลขที่ 1 : ', end='')
    number1 = int(input())
    return number1

def input_number2() :
    print('ป้อนตัวเลขที่ 2 : ', end='')
    number2 = int(input())
    return number2

def calculate_product(num1, num2) :
    return num1 * num2

def check_result(product) :
    if product > 5000 :
        return False
    return True

def show_result(num1, num2, product) :
    print(f'ผลคูณของ {num1} และ {num2} คือ {product}')
    print('-----------------------------')

print('-----------------------------')
product = 0
while True :
    num1 = input_number1()
    num2 = input_number2()
    product = calculate_product(num1, num2)
    show_result(num1, num2, product)
    if not check_result(product) :
        print('จบการทำงาน เนื่องจากผลคูณมากกว่า 5000')
        break
