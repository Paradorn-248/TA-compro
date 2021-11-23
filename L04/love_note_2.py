# name = input("Input name: ")
# re_name = name[::-1]
# for i in range(len(name)) :
#     for j in range(len(name)) :
#         if j==i or name[j] == name[i] :
#             print(name[j].upper(),end="")
#         else :
#             print(name[j],end="")
#     print(' ',end='')
#     for j in range(len(re_name)) :
#         if j == i or re_name[j] == re_name[i]:
#             print(re_name[j].upper(),end='')
#         else :
#             print(re_name[j],end='')
#     print()


# อีกวิธีที่ไม่ได้reverse
name = input("Input name: ")
for i in range(len(name)) :
    for j in range(len(name)) :
        if j==i or name[i]==name[j]:
            print(name[j].upper(),end="")
        else :
            print(name[j],end="")
    print(' ',end='')
    for j in range(len(name)-1,-1,-1) :
        if len(name)-j-1 == i or name[j] == name[len(name)-i-1]:
            print(name[j].upper(),end='')
        else :
            print(name[j],end="")
    print()

