def read_file(filename) :
    with open(filename,mode = 'r') as f :
        s = [line.strip().split() for line in f]
        for i in range(len(s)) :
            if (s[i][0] != 'List' and s[i][0] != 'Price') :
                s[i][1] = int(s[i][1])
        for line in f:
            print(line)
    return s

def read(filename) :
    with open(filename) as f :
        r = f.read()
        print(r)

def s_index(s,l) :
    n=0
    i=0
    while(s[i][0]!=l) :
        n += 1
        i += 1
    return n

def cal(s) :
    s1 = list()
    s2 = list()
    chk = True
    for i in range(1,len(s)) :
        if (s[i][0] == 'List' or s[i][0] == 'Price') :
            chk = False
            continue
        if (chk) :
            s1.append(s[i])
        else :
            s2.append(s[i])
    sum = 0
    for i in range(len(s1)) :
        sum += s1[i][1] * s2[s_index(s2,s1[i][0])][1]
    print("Total price:",sum)

filename = input("File name: ")
read(filename)
s = read_file(filename)
cal(s)