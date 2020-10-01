
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
    print_space()
    print("[5] Even or Odd?")
    print_space()
    print("[6] My age")
    print_space()
    print_space()
    print("[0] Exit")
    print_space()


#instruction

opc = ''
while( opc != '0' ):

    print_menu()

    opc = input('Please Choose An Option: ')

    if(opc == '6'):
        year = input("What year were you born? ")
        age = 2020 - int(year)
        print("You are " + str(age) + " years old.")
    
    elif(opc == '5'):
        num1 = input("Enter your number: ")
        if(int(num1) % 2 != 0):
            print(num1 + " is odd!")
        else:
            print(num1 + " is even!")

    if(opc != '0' and opc != '6' and opc != '5'):
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
    
    
 
print("Goodbye...")