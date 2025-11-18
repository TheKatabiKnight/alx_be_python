size = int(input('Enter the size of the pattern:'))
x = 1
y = 1
while x <= size:
        y = 1
        for  y in range (1, size+1):
            print("*", end="")
            y += 1
        print()
        x += 1   

