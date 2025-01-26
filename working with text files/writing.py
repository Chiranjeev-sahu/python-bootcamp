#used to overwrite the file and creating one if doesnt exist
#The 'w' mode overwrites the content of the file, so the file starts fresh with "New beginning".

with open('myfile.txt','w') as f:
    f.write('Just a line\n')
    f.write('Just a 2nd line\n')


#appending:will be created if it doesn't exist. It won't be overwritten if it exists. The 'a' mode adds content at the end of the file without modifying the existing content.
with open('myfile.txt', 'a') as f:
    f.write('Some text here.\n') 
    f.write('Another text')



#for reading and writing:
with open('myfile.txt', 'r+') as f: 
    f.write('Line added with r+\n')#=> adds to the beginning to append to a certion position do
with open('myfile.txt', 'r+') as f: 
    f.seek(5) 
    f.write('100')
    f.write('Line added with r+\n')
    f.seek(10) #reading can be done too
    print(f.read())