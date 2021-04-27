myStuff = {'book': 'alchemist', 'phone': 'iphone', 'Home': 'Bangladesh'}
print(myStuff['book'])

### intger key-value pair 
### print take index like list

x = {0: 100, 2: 400, 3: 500, 4: 600}
print(x[2])


### Orderness (not important)

a = {1: 100, 2: 200}
b = {2: 200, 1: 100}

print(a == b)


### concatenating two dictionaries
D = {'a': 100, "b": 200}
E = {"c": 200, 'd': 500}

newDic = D.copy()
newDic.update(E)
print(newDic)


