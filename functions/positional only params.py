def divide(numerator,denominator,/):
    return numerator/denominator

#correct usage
result=divide(10,2)

#incorrect
# res=divide(numerator=10,denominator=5)

def my_func(a,b,/,c,*,d,e=10):#here a,b are positional only, c can be both and d is keyword only and e is keyword only  with default args
    pass