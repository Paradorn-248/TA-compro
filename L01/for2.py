n = int(input("How many day : "))
summ = 0
percent = 5
for i in range(n) :
    a = float(input(f"Input price in day {i+1} : "))
    a = a*(100-percent)/100
    percent += 1
    summ += a
print(f"Summary price = {summ:.2f}")