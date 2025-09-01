print('===============================')
print(' โปรแกรมคำนวณเงินสุทธิ ')
print('===============================')
emp_id = input ('รหัสพักงาน : ')
emp_name = input('ฃื่อพนักงาน : ')
emp_salary = float( input('เงินเดือน : ') )
print('===============================')
tax = emp_salary * 7 / 100
insurance = emp_salary * 3 / 100
emp_salary_net = emp_salary - tax - insurance
print('รหัสพนักงาน {} ชื่อ {}'.format(emp_id, emp_name))
print('เสียภาษี {:,.2f} บาท ประกันสังคม {:,.2f} บาท' .format(tax, insurance))
print(f'สรุปได้เงินเดือนสุทธิ {emp_salary_net:,.2f} บาท')
print('===============================')