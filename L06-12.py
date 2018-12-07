def myfunc(a,b,c=7, *args,**kwargs):
    args_raw,kwargs_raw =args,kwargs
    for i in args:
        print (i)
    result=a+b-c
    return result
myfunc(2,3)
