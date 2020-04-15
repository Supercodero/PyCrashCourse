with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open('programming.txt','a') as file_write_object:
    file_write_object.write("I also love finding meaning in large datasets.\n")