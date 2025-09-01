print('===============================')
print(' โปรแกรมแสดงข้อความต้อนรับนักศึกษา ')
print('===============================')
student_name = input('ป้อนชื่อนักศึกษา : ')
student_class = float(input('ป้อนชั้นปีการศึกษา : ') )
if student_class == 1 :
    print(f'Welcome Freshman')
elif student_class == 2 :
    print(f'Welcome Sophomore')
elif student_class == 3 :
    print(f'Welcome Junior')
elif student_class == 4 :
    print(f'Welcome Senior')
else :
    print('Oh, no ....')