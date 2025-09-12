# 3. no parameter have return
'''
def  func_name( ) :
    คำสั่ง
    คำสั่ง
    .......
'''
def func_e( ) :
    print('Hello...')
    return 'Hi...'
 
def func_f( ) :
   return 'Wow...', 'Woo...', 99999
 
print( func_e() )

xx = func_e( )
print(xx)

a, b, c = func_f()
print(a)
print(b)
print(c)