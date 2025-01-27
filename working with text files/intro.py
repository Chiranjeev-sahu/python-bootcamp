f=open("configuration.txt",'r')
content=f.read()
print(content)

#to close:
f.close()
print(f.closed)

#always close the files