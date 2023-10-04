# Creating a yfunction

def greetings_function():
    print("welcome user")

greetings_function()

# passing parameters

def greeting_user (name):
    print("welcome" + name)

greeting_user("john")

# Passing int values

def passing_int(numb):
    print("the number is " + str(numb))

passing_int(34)

# passing mutliple arguement

def multiple_arg(name, age):
    print("welcome" + name + ". you are " + str(age) + "years old")

multiple_arg("John", 27)

# unknown amount of parameters
def unkown_arg(*name):
    print("welcome" + name[1] )

unkown_arg("John", "dearborn", "Tom")

# passing mutliple arguement using varaible name

def multiple_arg_wn(name, age):
    print("welcome" + name + ". you are " + str(age) + "years old")

multiple_arg_wn(name="jone", age=27)

# dyanmic renderimg

# def login (db, cd):
#    print("Hello" + db + "you are welcome our "+ str(cd) + "user" )

#db = input("what is your fullname")
#cd = input("pick a number" )

#slogin(db, cd)

# return keyword

def my_function():
    return 5 + 4
print(my_function())

def addNum(numb1, numb2):
    return numb1 + numb2
print(addNum(2,3))

# dynamically use return Keyword
def add_numbers(number1, number2):
    return number1 + number2
number1 = int(input("number 1 "))
number2 = int( input("number 2 "))

print(add_numbers(number1, number2))