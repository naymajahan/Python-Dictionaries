#### 1st program::: This program counts the frequency of characters on a string


text = "this is a simple text to TEST the code"

letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i]+1

print(letters)


### using prety print

import pprint as pp
text = "this is a simple text to TEST the code"

letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i]+1

pp.pprint(letters)





##### This program simulates a password protected app access


passwordBank = {'Nayma': 123, 'Naim': 1234, 'Shoshe': 12345}
matched = False
x = 0 ## Loop control variable
print('Enter your Name')

while  x < 5:
    name = input()
    if name in passwordBank:
        for i in range(0,3):
            print('Enter your password')
            password = input()
            if int(password) in passwordBank.values():
                matched = True
                print('Access Granted')
                break
            else:
                print('Wrong password. Enter Again: '+' You Have '+str(2-i+' tries left'))

    else:
        print('There is no such name in the passwordBank. Try again')
    x = x+1
    if matched:
        break




## Program -3 : This Program simulates a phone-book

contactNo = {'shoshe': 000, 'naim': 111, 'oishe': 222}
x = 0

while x < 5:
    print('Enter your name (Press ENTER to exist): ')
    name = input()

    if name == "":
        break

    if name in contactNo:
        print("The contact number of " + name + " is " + str(contactNo[name]))
    else:
        print("There is no such name in the phone-book. Do you want to add it ? ")
        desc = input()

        if desc == "yes":
            print('Enter the Number')
            num = input()
            contactNo[name] = num
            print('Dictionary Updated')
        elif desc == 'no':
            print('Do you want to quit ?')
            desc = input()
            if desc == 'yes':
                break
            else:
                print('Keep searching')

    x = x + 1


