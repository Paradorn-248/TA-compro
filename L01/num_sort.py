a, b, c, d = map(int, input().split()) #คือการให้ค่าตัวแปรหลายตัวในทีเดียว map(func,*iterible(เช่น list)) ตรงส่วนของfunctionบอกแค่ชื่อพอ
one, two, three, four = 0, 0, 0, 0

if a < b:
    if c > b:
        one, two, three = a, b, c
    else:
        if a < c:
            one, two, three = a, c, b
        else:
            one, two, three = c, a, b
else:
    if c > a:
        one, two, three = b, a, c
    else:
        if b < c:
            one, two, three = b, c, a
        else:
            one, two, three = c, b, a
if d <= one <= two <= three:
    one, two, three, four = d, one, two, three
elif one <= d <= two <= three:
    one, two, three, four = one, d, two, three
elif one <= two <= d <= three:
    one, two, three, four = one, two, d, three
else:
    one, two, three, four = one, two, three, d

print(f'{one} {two} {three} {four}')
