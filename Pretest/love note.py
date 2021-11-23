name = input()
for i in range(len(name)) :
    for j in range(len(name)) :
        if i == j :
            print(name[j].upper(),end='')
        else :
            print(name[j],end='')
    print("")