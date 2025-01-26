# used for taking var num of args

#*args=> any no. of args
def average(a,b,*args):
    print(f'args  is {args}')
    return (a+b+sum(args))/(2+len(args))

print(average(4,5,6,7))


def concatenate(*args):
    result=''
    for tmp in args:
        result+=tmp

r=concatenate('Python','is','great')
print(r)




# **kwargs=> any no. of key value pair

def my_fucn(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'k is {k} and v is {v}')


my_fucn(name='Jon',age=40)


#example usecase:
def connect(ip,port,username,password):
    print(ip,port,username,password)

linux_server={'ip': '200.0.10.1', 'port': 22, 'username': 'admin1', 'password': 'secretPass'}

connect(**linux_server)#dictionary unpacking