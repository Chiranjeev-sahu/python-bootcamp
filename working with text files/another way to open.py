with open('configuration.txt') as file:
    content=file.read()
    print(content)
    print(file.closed)#=>false

print(file.closed)#=>True
# file.read()#=>nothing because file is closed

