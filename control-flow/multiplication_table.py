number = int(input('Enter a number to see its multiplication table:'))
for table in range (1, 11):
    multiplication = table * number
    print(number, ' * ', table, ' = ',multiplication )