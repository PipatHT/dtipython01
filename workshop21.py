print('===============================')
print(' โปรแกรมคำนวณค่าคอมมิชชั่นของพนักงานขาย ')
print('===============================')
commit_id = input('ป้อนรหัสพนักงาน : ')
commit_name = input('ป้อนชื่อพนักงาน : ')
commit_money = int(input('จำนวนเงินยอดขายของฃื่อพนักงาน : ') )
if commit_money == 1000 :
    commit_money_net = commit_money + 0
    print(f'พนักงาน {commit_name} รหัสพักงาน {commit_id} ค่าคอมมิชชั่น {commit_money_net:,.2f} บาท จากยอดขาย {commit_money:,.2f} บาท')
elif commit_money == 1001 <= 2000 :
    commit_money_net = commit_money - (commit_money * 1 / 100)
    print(f'พนักงาน {commit_name} รหัสพักงาน {commit_id} ค่าคอมมิชชั่น {commit_money_net:,.2f} บาท จากยอดขาย {commit_money:,.2f} บาท')
elif commit_money == 2001 <= 3000 :
    commit_money_net = commit_money - (commit_money * 3 / 100)
    print(f'พนักงาน {commit_name} รหัสพักงาน {commit_id} ค่าคอมมิชชั่น {commit_money_net:,.2f} บาท จากยอดขาย {commit_money:,.2f} บาท')
else :
    commit_money_net = commit_money - (commit_money * 5 / 100)
    print(f'พนักงาน {commit_name} รหัสพักงาน {commit_id} ค่าคอมมิชชั่น {commit_money_net:,.2f} บาท จากยอดขาย {commit_money:,.2f} บาท')
print('===============================')