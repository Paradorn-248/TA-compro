win = input("Enter lucky number : ")
n = int(input("Enter amount of candidate : "))
id = []
index = []
nub = [0 for _ in range(n)]

for i in range(n) :
    add = input(f"Enter ID card number {i+1}: ")
    id.append(int(add))
    for j in range(len(add)) :
        if add[j] == win :
            nub[i] += 1

chk = 0
maxx = max(nub)
for i in range(n) :
    if maxx == nub[i] :
        chk += 1
        index.append(i)

if chk > 1 :
    res = 0
    for i in range(chk) :
        if res < id[index[i]] :
            res = id[index[i]]
    print("Winner :",res)

else :
    print("Winner :",id[index[0]])

    