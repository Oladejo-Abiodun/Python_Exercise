# ASS 1
# WRITE A PYTHON PROGRAM TO GET A NUMBER FROM USER E.G. 15. GENERATE NUMBER
# FROM 1 TO UP TO USER ENTERED NUMBER. AND FIND ADDITION OF ALL NUMBERS FROM 1 
# TO USER ENTERED NUMBER.

# APPROACH 1 
user = int(input("Enter your number here. "))

i = 1
count = 0

while i <= user:
    print(i)
    i += 1
    count += i
print("The total of the entered number by the user is: "+str(count))

# APPROACH 2 
user = int(input("Enter your number here: "))

def num():
    i = 1
    count = 0
    while i <= user:
        count += i
        i += 1
    return count

result = num()
print("The total of the entered number by the user is: " + str(result))


# ASS 2
# WRITE A PYTHON PROGRAM TO GET A STRING FROM USER AND DISPLAY STRING IN REVERSE ORDER

# APPROACH 1 
def reverse():
    a = input("Enter any words here. ")
    word = ""
    for i in a:
        word = i + word
    print(word)

reverse()

# APPROACH 2

def reverse(string):
    word = ""
    for i in string:
        word = i + word
    return word

input_string = input("Enter any words here: ")
reversed_string = reverse(input_string)
print(reversed_string)

