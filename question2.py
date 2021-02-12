pin_number = 1234
supplied_pin = int(input("Enter your pin: "))

x = 0
while x < 2:
    if pin_number == supplied_pin:
        print('You have access!')
        break
    else:
        input("Enter your pin: ")
    x += 1