### printing only values

identity = {'Name': 'Nayma', 'Age': "21", "job": "student"}

for i in identity.values():
    print(i)


# printing Keys

for i in identity.keys():
    print(i)

### Printing Both Keys and values

for i in identity.items():
    print(i)


### Converting values and keys in a list

x = list(identity.keys())
y = list(identity.values())

print(x)
print(y)


### A handy Trick 

for k, v in identity.items():
    print('key: '+k+' value: '+v)

#### Use of "in" keyword
### Checking present or not

print('Name' in identity)
print("pop" in identity)

print('shoshe' in identity.values())
print("Age" in identity.keys())


### The Get () method

print(str(identity.get('Name', 'Default')))
print(str(identity.get('height', 'Default')))


#### The setdefault() method

print(identity.setdefault('Name', 'Cosmos'))
print(identity.setdefault('height', '5ft'))
print(identity)


