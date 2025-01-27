from typing import TypedDict

class movie(TypedDict):
    title:str
    year:int
    rating:float

my_movie:movie={
    'title':'Inception',
    'year':2010,
    'rating':8.8
}

print(my_movie['title'])
my_movie['rating']=9

from typing import TypedDict


#------------------
# Define the Address TypedDict
class Address(TypedDict):
    street: str
    city: str
    zip: str

# Define the User TypedDict
class User(TypedDict):
    username: str
    email: str
    address: Address

# Create an instance of the User TypedDict
my_user: User = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'address': {
        'street': '123 Main St',
        'city': 'NYC',
        'zip': '12345'
    }
}

# Print the city from the address
print(my_user['address']['city'])
