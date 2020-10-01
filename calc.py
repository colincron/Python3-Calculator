
def print_space():
    print(" ")

def print_menu():
    print("*" * 20)
    print_space()
    print("  Python Calculator")
    print_space()
    print("*" * 20)

    print_space()
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Exponents")
    print_space()
    print("[8] Even or Odd?")
    print_space()
    print("[9] My age")
    print_space()
    print_space()
    print("[0] Exit")
    print_space()


#instruction

opc = ''
while( opc != '0' ):

    print_menu()

    opc = input('Please Choose An Option: ')

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        num1 = input("First number: ")
        num2 = input("Second number: ")

    if(opc == '1'):
        res = float(num1) + float(num2)
        print("Result: " + str(res))

    elif(opc == '2'):
        res = float(num1) - float(num2)
        print("Result: " + str(res))

    elif(opc == '3'):
        res = float(num1) * float(num2)
        print("Result: " + str(res))

    elif(opc == '4'):
        if(float(num2) != 0):
            res = float(num1) / float(num2)
            print("Result: " + str(res))
        else:
            print("WARNING -- YOU WILL DESTROY THE UNIVERSE")
    
    elif(opc == '5'):
        base = input("Enter base number: ")
        exponent = input("Enter exponent: ")
        res = float(base) ** float(exponent)
        print("The solution is: " + str(res))
    
    elif(opc == '8'):
        num1 = input("Enter your number (not 0): ")
        if(float(num1) == 0):
            print("Bruh, I said not 0...")
        elif(float(num1) % 2 != 0):
            print(num1 + " is odd!")
        else:
            print(num1 + " is even!")
    
    elif(opc == '9'):
        year = input("What year were you born? ")
        age = 2020 - int(year)
        print("You are " + str(age) + " years old.")

print("Goodbye...")