n = input()
tell = list()
chk = True
bad_num = ["20","13","18","80","31","93"]
for i in range(len(n)) :
    tell.append(int(n[i])) 
if tell[1] == 8 :
    if(sum(tell)%13==0 and sum(tell)<=56) :
        print("Have bad luck.")
    else :
        print("Have good luck.")
elif tell[1] == 9:
    for i in range(len(tell)-2) :
        if (str(tell[i]) + str(tell[i+1])) in bad_num :
            print("Have bad luck.")
            chk = False
            break
    if chk == True :
        print("Have good luck.")

# 0864516414 bad
# 0811459423 good 37
# 0897869874 good 66
# 0879876956 good 65
# 0954891326 bad 
# 0935680136 bad 1 ครั้ง
# 0941652349 good