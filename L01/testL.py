height = int(input())
arrow = input('Arrow : ')
stick = input('Stick : ')

for i in range(height+1):
    print(' '*(height-(i))+arrow*((2*(i)-1)))
for i in range(height):
    print((height-1)*' '+stick)