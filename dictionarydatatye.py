# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d2= {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d2['name'])

# Accessing a element using get
print(d2.get(3))
