def sen_pa() :
    print('--------------------')

def show_program_name( ) :
    print('--------------------')
    print(' ตรวจสอบควันดำ ')
    print('--------------------')

def input_car_Info( ) :
    car_owner = input('ป้อนชื่อเจ้าของรถ : ')
    car_number = input('ป้อนทะเบียนรถ : ')
    car_carbon = int( input('ป้อนปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ : ') )
    return car_owner, car_number, car_carbon

def show_result(car_owner, car_number, car_carbon, reseult) :
    print(f'คุณ {car_owner} ทะเบียนรถ {car_number}')
    print(f'ก๊าซ {car_carbon} สรุป: {reseult}')

def check_carbon(car_owner, car_number, car_carbon, reseult) :
    if car_carbon > 678.55 :
        show_result(car_owner, car_number, car_carbon, 'ไม่ผ่านเกณฑ์')
    else:
        show_result(car_owner, car_number, car_carbon, 'ผ่านเกณฑ์')

show_program_name( )
car_owner, car_number, car_carbon = input_car_Info( )
sen_pa()
check_carbon(car_owner, car_number, car_carbon)
sen_pa()