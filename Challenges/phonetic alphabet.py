dictionary=dict()
with open('/media/chiru/New Volume/Python/python-bootcamp/Challenges/phonetic_alphabet.csv') as f:
    content=f.read().splitlines()
    for item in content[1:]:
        item.split(',')
        letter,word=item.split(',')
        dictionary[letter]=word
    print(dictionary)

code=input("Enter something for phonetic albhabet code:").upper()
print(code,end='=>')
for i in code:
    if i in dictionary:
        print(dictionary[i],end='    ')
    else:
        print('Invalid input')