from datetime import datetime

print('+++++++++++++++++++++++++++++++')
print(' โปรแกรมคำนวณอายุพนักงานในโรงงาน ')
print('+++++++++++++++++++++++++++++++')

while True :
    emp_name = input('ชื่อพนักงาน : ')
    if emp_name.upper() == 'SAU' :
        break
    emp_year = int(input('ปีเกิด (พ.ศ.) : '))
    emp_age = (datetime.now().year + 543) - emp_year
    print(f'คุณ {emp_name} เกิดปีนี้ {emp_year} อายุ {emp_age} ปี')
    print('+++++++++++++++++++++++++++++++')

print('+++++++++++++++++++++++++++++++')
print('ขอบคุณที่ใช้บริการโปรแกรมของเรา DTI-SAU หากมีปัญหาโทร. 1111 คิด 500 บาท')
print('+++++++++++++++++++++++++++++++')