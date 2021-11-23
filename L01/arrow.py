a= int(input())
head = input("Arrow : ")
body = input("Stick : ")
for i in range(a) :
    print(" "*(a-i)+head*(2*i+1))
for i in range(a) :
    print(" "*a+body)