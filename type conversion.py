#1 mile=1.609
miles=input('Enter distance:')
print(type(miles))

# km=miles*1.609
# print('Distance in km:',km)#error will be recieved


#conversion
miles=float(miles)
km=miles*1.609
print('Distance in km:',km)#this will work fine


a=10
b=2.5
c='8.2'


#all can be converted to str but vice versa is not true
#str=> int