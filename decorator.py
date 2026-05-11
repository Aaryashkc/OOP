def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func

@my_decorator   #the function above my decorator is made a decorator here
def hello():
    print ('Hello World!')

hello()