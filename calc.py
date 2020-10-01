
def print_space():
    print(" ")

def print_menu():
    print("*" * 21)
    print_space()
    print("  Python Calculator")
    print_space()
    print("*" * 21)

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

def press_enter():
    input("Press Enter to continue...")


#instruction

green_text = "\033[32m"
red_text = "\033[31;1m"
color_default = "\033[m"

opc = ''
while( opc != '0' ):

    print_menu()

    opc = input('Please Choose An Option: ')

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        num1 = input(green_text + "First number: " + color_default)
        num2 = input(green_text + "Second number: " + color_default)

    if(opc == '1'):
        res = float(num1) + float(num2)
        print(red_text + "Result: " + str(res) + color_default + "\n")
        press_enter()

    elif(opc == '2'):
        res = float(num1) - float(num2)
        print(red_text + "Result: " + str(res) + color_default + "\n")
        press_enter()

    elif(opc == '3'):
        res = float(num1) * float(num2)
        print(red_text + "Result: " + str(res) + color_default + "\n")
        press_enter()

    elif(opc == '4'):
        if(float(num2) != 0):
            res = float(num1) / float(num2)
            print(red_text + "Result: " + str(res)  + color_default +  "\n")
            press_enter()
        else:
            print(red_text + "WARNING -- YOU WILL DESTROY THE UNIVERSE!" + color_default +  "\n")
            press_enter()
    
    elif(opc == '5'):
        base = input("Enter base number: ")
        exponent = input("Enter exponent: ")
        res = float(base) ** float(exponent)
        print(red_text + "The solution is: " + str(res) + color_default + "\n")
        press_enter()
    
    elif(opc == '8'):
        num1 = input("Enter your number (not 0): ")
        if(float(num1) == 0):
            print(red_text + "Bruh, I said not 0..." + color_default + "\n")
            press_enter()
        elif(float(num1) % 2 != 0):
            print(red_text + num1 + " is odd!" + color_default + "\n")
            press_enter()
        else:
            print(red_text + num1 + " is even!" + color_default + "\n")
            press_enter()
    
    elif(opc == '9'):
        year = input("What year were you born? ")
        age = 2020 - int(year)
        print(red_text + "You are " + str(age) + " years old." + color_default + "\n")
        press_enter()

print("Goodbye...")