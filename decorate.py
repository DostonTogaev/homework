# Decorates

def math_decorate(func):
    def wrapper(*args, **kwargs):
        print("called decorate function")
        result = func(*args,**kwargs)
        print(result)
        print("decorate function finished")
        return result
    return wrapper

@math_decorate
def math(n):
    if n%2 == 0:
        return n**2


print(math(10))

import  datetime
now = datetime.datetime.now()
def time(func):
    def wrapper(*args, **kwargs):
        natija = func(*args,**kwargs)
        print(natija)
        return natija
    return wrapper

@time
def info(n):

    return 2024-n
print(info(1999))