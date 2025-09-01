print('===============================')
print(' โปรแกรมตรวจสอบข้อมูลสายรถเมล์ ')
print('===============================')
bus_number = float( input('ป้อนสายรถรถเมล์ : ') )
print('===============================')
if bus_number == 57 :
    print(f'สาย {bus_number:,.2f} ไป ปิ่นเกล้า บางขุนนนท์ ')
elif bus_number == 3 :
    print(f' สาย {bus_number:,.2f} ไป สนามหลวง ลาดพร้าว ')
elif bus_number == 71 :
    print(f' สาย {bus_number:,.2f} ไป หัวลำโพง เยาวราช ')
elif bus_number == 56 :
    print(f' สาย {bus_number:,.2f} ไป บางลำพู สะพานกรุงธน ')
elif bus_number == 539 :
    print(f' สาย {bus_number:,.2f} ไป อนุสวรีย์ชัย สามเสน ')
else :
    print('ยังไม่มีข้อมูลสายรถเมล์ที่สอบถาม')
print('===============================')