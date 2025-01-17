# Define a dictionary with various key-value pairs
person = {'name': 'john', 'age': 30, (1, 2, 3): 100}

# Print the number of key-value pairs in the dictionary
print(len(person))

# Demonstrate mutability: Update the value associated with the key 'name'
person['name'] = 'Dan'
print(person)

# Add a new key-value pair to the dictionary
person['location'] = 'Berlin'
print(person)

# Extract the value associated with the key 'age'
a = person['age']  # If the key doesn't exist, this will raise a KeyError
print(a)

# Safely retrieve a value using .get(): If the key doesn't exist, return a default message
value = person.get('city', 'Key does not exist')
print(value)

# Remove and return the value associated with the key 'name' using .pop()
name = person.pop('name')
print(name, person)

#popitem()=>returns the last inserted key-value pairs as a tuple
print(person.popitem())


#del
del person['age']#gives key error if the key is absent
print(person)

#accessing
germany={
    'cities':['hmburg','berlin','munich'],
    'info':{'population':83_000_000,'person':['Einsterin','Bach','Gauss']}
}

print(germany['cities'][1])#=>to access berlin
print(germany['info']['people'][-1])#to access Gauss

# accessing in list of dictionaries
countries=[
        {
        'cities':['hmburg','berlin','munich'],
        'info':{'population':83_000_000,'person':['Einsterin','Bach','Gauss']}
   }, 

    {
        'cities':['Paris','Lyon','Boreduax'],
        'info':{'population':83_000_000,'person':['Einsterin','Bach','Gauss']}
    }

]

print(countries[0]['cities'])
print(countries[1]['info'][1])