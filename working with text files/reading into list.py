#1. f.read().splitlines()
with open('configuration.txt') as f:
    content= f.read().splitlines()
    print(content)
print('#'*50)

#2. f.readlines()
with open('configuration.txt') as f:
    content= f.readlines()
    print(content)#=> returns lines with \n at end while can be solved by:
print('#'*50)


with open('configuration.txt') as f: 
    print(f.readline(),end='')#=> prints one line at a time
print('#'*50)


#3. list(f) 
with open('configuration.txt') as f:
    content=list(f)
    print(content)


#4. iterat over a file

with open('configuration.txt') as f:
    for line in f:
        print(line,end='')