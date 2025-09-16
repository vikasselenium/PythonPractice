'''
Write a  program
String str = "12345"
output -15 (All numbers get added but need to convert string to int, by traversing each char)

'''

my_string="12345"
total = 0
for char in my_string:
    if char.isdigit():
        total=total+int(char)
print(total)