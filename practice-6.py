####a simple bankig system database

####a simple bankig system database

bankDatabase = {'naim': 2, 'shoshe': 5, 'mitu': 10, 'oishe': 12, 'nayma': 16}

print('Welcome to the bank')
while True:
    print("  "+'1.VIEW BALANCE')
    print('  '+'2.VIEW ALL BANK INFO')
    print("  "+"3.UPDATE BALAMCE")
    print('  '+'4.EXIT')


    desc = input()
    if desc == '1':
        print('Enter your name, please ')
        k = input()

        if k in bankDatabase.keys():
            print(k+'your bank balamce is '+str(bankDatabase[k]))
        else:
            print('The user name does not exist. Would you like to add the name ??')
            desc = input()

            if desc == 'yes':
                k = input('ENTER YOUR NAME PLEASE')
                v = input('ENTER YOUR BALANCE PLEASE')
                bankDatabase.update({k: v})
            else:
                print('Would you like to exit? ')
                desc = input()
                if desc == 'yes':
                     break


    elif desc == "2":

      for k, v in bankDatabase.items():
          print('USERNAME: '+str(k)+' Bank Balance: '+str(v))

    elif desc == "3":
        print("Enter your name please: ")
        k = input()
        if k in bankDatabase.keys():
            print("Do you want to ADD or SUBSTRACT from your savings?? ")
            desc = input()
            if desc == 'ADD':
                tempBalance = bankDatabase[k]
                extra = input('ENTER THE AMOUNT YOU WANT TO ADD')
                bankDatabase[k] = tempBalance+int(extra)
                print('BALANCE UPDATED. IT IS: ')
                print(bankDatabase[k])
            elif desc == 'SUBSTRACT':
                tempBalance = bankDatabase[k]
                extra = input('ENTER THE AMOUNT YOU WANT TO SUBSTRACT: ')
                bankDatabase[k]= tempBalance-int(extra)
                print('BANK BALAMCE UPDATED, IT IS : ')
                print(bankDatabase[k])
        else:
            print('THere is no such account in the bank database. ')


    elif desc =="4":
       break




### Write a program to print the unique values of a dictionary.

 = {1: 1, 2: 2, 3: 1, 4:34}
b = {}
count = {}
for i in a.values():
    count.setdefault(i, 0)
    count[i] = count[i]+1

i = 0
for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i+1

for i in b.values():
    print(i,end=" ")


    
