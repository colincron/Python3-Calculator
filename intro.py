
def test():
    print('Im a function')

def separator():
    print("-------------")


print('Hello Python')

separator()

# variables
name = 'Colin'
last = "Cron"
age = 31
found = False
total = 23.4
products = ['apples', 'bananas']

print(name)
print(name + " " + last)

print(age + age)

print(name + name)

print(name + str(age))

print(products)

separator()

# math operations
print(age - 10)
print(age + 10)
print(age * 2)
print(age / 2)
print(age % 2)

separator()

# if statement
if(age < 80):
    print("You're still young!")
elif(age > 80):
    print("You're pretty old")
else:
    pass
