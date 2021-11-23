
# """
# เขียนฟังก์ชั่นแสดงว่าน้ำแต่ละชนิดนนั้นราคาแก้วละกี่บาท รับจำนวนว่าซื้อน้ำกี่ชนิด และรับค่าว่าซื้อน้ำชนิดไหน กี่แก้ว ส่งค่าออกมาเป็นจำนวนเงินทั้งหมดที่ต้องจ่าย

# Late = 40
# Espresso = 45
# Americano = 50
# Mocca = 55
# Cappuccino = 60 

# """
# # แสดงเมนูกาแฟของทางร้าน รับลำดับที่ของเมนูที่ลูกค้าสั่ง และจำนวนแก้วที่ลูกค้าสั่ง จนกว่าลำดับที่ของเมนูจะเท่ากับ0 จากนั้นแสดงและส่งค่าออกมาเป็นจำนวนเงินทั้งหมดที่ต้องจ่าย
# def sum_price() :
#     print("Menu\n0. Finish\n1. Latte = 40\n2. Espresso = 45\n3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60")
#     sum = 0
#     while 1 :
#         coffee = int(input("coffee : "))
#         if coffee != 0 :
#             if coffee == 1 :
#                 amount = int(input("amount : "))
#                 sum += 40*amount
#             if coffee == 2 :
#                 amount = int(input("amount : "))
#                 sum += 45*amount
#             if coffee == 3 :
#                 amount = int(input("amount : "))
#                 sum += 50*amount
#             if coffee == 4 :
#                 amount = int(input("amount : "))
#                 sum += 55*amount
#             if coffee == 5 :
#                 amount = int(input("amount : "))
#                 sum += 60*amount
#         else :
#             break
#     print("total price :",sum)
#     return sum

# # ฟังก์ชันรับจำนวนเงินที่ลูกค้าจ่ายมา และแสดงผลลัพธ์ว่าเราต้องจ่ายเงินทั้งหมดกี่บาท ทอนเงินกี่บาท และทอนแบงค์/เหรียญแต่ละชนิดกี่ใบ/เหรียญ
# def change(total_price,pay) :
#     change_price = pay-total_price
#     print("customer's change :",change_price)
#     bank = [1000,500,100,50,20,10,5]
#     for i in range(len(bank)) :
#         n = change_price//bank[i]
#         if n!=0 :
#             print(f"change {bank[i]} : {n}")
#         change_price %= bank[i]
        
# total_price = sum_price()
# pay = int(input("customer pay : "))  
# change(total_price,pay)


# ######################################## check function
# # ::elab:begincode hidden=True
# # check = input()
# # if check == '01':
# #     print(sum_price())
# # elif check =='02' :
# #     change(130,200)
# # ::elab:endcode
def sum_price():
  print('Menu')
  print('0. Finish')
  print('1. Latte = 40')
  print('2. Espresso = 45')
  print('3. Americano = 50')
  print('4. Mocca = 55')
  print('5. Cappuccino = 60')
  z=0
  while True:
    c = int(input('coffee : '))
    if c == 0:
      break
    n = int(input('amount : '))
    if c == 1:
      total = (40*n)
    if c == 2:
      total = (45*n)   
    if c == 3:
      total = (50*n)
    if c == 4:
      total = (55*n)
    if c == 5:
      total = (60*n)
    z +=total
  print(f'total_price : {z}')
  return z
def change(total_price,pay):
 c = pay -total_price
 if c//1000==0:
  print(f'change 1000 : {c//1000}')
 if c//100==0:
  print(f'change 100 : {c//100}')
 if c//20==0:
  print(f'change 20 : {c//20}')
 if c//10==0:
  print(f'change 10 : {c//10}')
 if c//5==0:
  print(f'change 5 : {c//5}')
 if c//1==0:
  print(f'change 1 : {c//1}')
a=sum_price()
change(a,200)