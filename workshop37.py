def show_program_name( ) :
    print('--------------------')
    print(' โปรแกรมตรวจสอบอายุ ')
    print('--------------------')
    
def input_name() :
    print('ป้อนชื่อของคุณ : ', end='')
    name = input()
    return name

def input_year() :
    print('ป้อนปี พ.ศ. เกิดของคุณ : ', end='')
    year = int(input())
    return year

def cal_age(year) :
    current_year = 2568  
    age = current_year - year
    return age

def check_age(age) :
    if age >= 55 :
        print('คุณแก่แล้ว...')
    else :
        print('คุณยังไม่แก่...')

print('-----------------------------')
name = input_name()
year = input_year()
age = cal_age(year)
print(f'คุณ {name} อายุ {age} ปี')
check_age(age)
print('-----------------------------')
