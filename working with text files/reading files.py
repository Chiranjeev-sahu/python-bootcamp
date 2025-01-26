# f=open('configuration.txt')

# content=f.read(5)
# print(content)#=>hostn

# content =f.read(3)
# print(content)#=>ame

# #it somehow remembers where it left


# # to know the cursor position
# print(f.tell())

# #to move the cursor to a certain position
# f.seek(2)
# content=f.read(3)
# print(content)#=>stn


f=open('configuration.txt')
print(f.read())
#do stuff
print('#'*50)
print(f.read())#=> gives nothing

# to solve this use f.seek:
f.seek(0)
print(f.read())


