s1 = 'I am Learning python programming'
l1=s1.split()
print(l1)

#can also give delimiter
s2 = 'I am Lea:rning pyth:on prog:rammi:ng'
l2=s2.split(':')#can also give delimiter
print(l1)


#join
ip_list=['123.435.576','453.754.432','655.234.756']
ip_str= ' '.join(ip_list)
print(ip_str)

#in place of blank separater we can add that too like this => ip_str= ','.join(ip_list)
