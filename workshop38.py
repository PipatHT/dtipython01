def show_program_name( ) :
    print('--------------------')
    print(' โปรแกรมตรวจสอบสายรถเมล์ ')
    print('--------------------')

def input_bus_number() :
    print('ป้อนหมายเลขสายรถเมล์ : ', end='')
    number = input()
    return number

def check_bus_route(number) :
    if number == '57' :
        print('สาย 57 ไปปิ่นเกล้า บางขุนนนท์')
    elif number == '3' :
        print('สาย 3 ไปสนามหลวง ลาดพร้าว')
    elif number == '71' :
        print('สาย 71 ไปหัวลำโพง เยาวราช')
    elif number == '56' :
        print('สาย 56 ไปบางลำพู สะพานกรุงธน')
    elif number == '539' :
        print('สาย 539 ไปอนุสวรีย์ชัย สามเสน')
    else :
        print('ยังไม่มีข้อมูลสายรถเมล์ที่สอบถาม')

def main() :
    print('-----------------------------')
    bus_number = input_bus_number()
    check_bus_route(bus_number)
    print('-----------------------------')

main()
