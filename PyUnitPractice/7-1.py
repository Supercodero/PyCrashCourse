car = input("What kind of cars do you want?")
print("Let me see if I can find you a"+car)

person_num = input("How many people there now?")
person_num = int(person_num)
if person_num > 8:
    print("Sorry, There are not empty table here")
else:
    print("Welcome!")

num = input("please write your favorite number:")
num = int(num)
if num % 10 == 0:
    print("Yes!")
else:
    print("Oh, no!")