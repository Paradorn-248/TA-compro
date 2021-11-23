data = dict()  # ปริ้นรหัสนักศึกษาของคนที่มีพ่อแม่เงินเดือนมากกว่าinput น่าจะอัพเกรดโจทย์ได้ แต่เดะค่อย

while 1:
    id = input("Student ID : ")    
    if id == '0' :
        break
    salary = int(input("years : "))
    data.update({id: salary})

a = int(input("Separate year: "))
for k,v in data.items():
    if v >= a :
        print(k)
    
