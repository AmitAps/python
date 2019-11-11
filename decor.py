def null_decorator(func):
    return func

#def greet():
    #return 'Hello!'

#greet = null_decorator(greet)

@null_decorator
def greet():
    return 'Hello, Amit'
