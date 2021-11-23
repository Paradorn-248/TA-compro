name = input("Input name: ")
for i in range(len(name)) :
    for j in range(len(name)) :
        if j==i :
            print(name[j].upper(),end="")
        else :
            print(name[j],end="")
    print()
