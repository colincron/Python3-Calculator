
def print_space():
    print(" ")

def print_menu():
    print(cyan_text + "*" * 21 + color_default)
    print_space()
    print(cyan_text + "  Python Calculator" + color_default)
    print_space()
    print(cyan_text + "*" * 21 + color_default)

    print_space()
    print(blue_text + "[1] Add" + color_default)
    print(yellow_text + "[2] Subtract" + color_default)
    print(blue_text + "[3] Multiply" + color_default)
    print(yellow_text + "[4] Divide" + color_default)
    print(blue_text + "[5] Exponents" + color_default)
    print_space()
    print(red_text + "[8] Even or Odd?")
    print_space()
    print("[9] My age" + color_default)
    print_space()
    print_space()
    print(red_underline + "[0] Exit" + color_default)
    print_space()

def press_enter():
    input(yellow_text + "Press Enter to continue...\n\n\n" + color_default)


#instruction

blue_text = "\033[34;1m"
yellow_text = "\033[33m"
green_text = "\033[32;1m"
red_text = "\033[31;1m"
cyan_text = "\033[36;1m"
red_underline = "\033[31;5m"

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
            print(red_text + "\n\n\nWARNING -- YOU WILL DESTROY THE UNIVERSE!" + color_default +  "\n")
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