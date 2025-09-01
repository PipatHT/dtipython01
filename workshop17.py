from datetime import datetime

print('===============================')
print(' โปรแกรมตรวจสอบวัยวุฒิ ')
print('===============================')

your_name = input('ป้อนชื่อ ==>> ')
your_yearborn = int(input('ป้อนปีเกิด(พ.ศ.) ==>> '))

print('===============================')

your_age = (datetime.now().year + 543) - your_yearborn

if your_age >= 55 :
    print('คุณ {} อายุ {} ปี แก่เเล้วนะ'.format(your_name, your_age))
    print('ยังไหวอยู่มั้ย...')
else :
    print('คุณ {} อายุ {} ปี ยังไม่แก่เลย'.format(your_name, your_age))
    print('ยังเด็กอยู่นะ...')