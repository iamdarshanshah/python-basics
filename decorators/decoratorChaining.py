# Aplying multiple decorator functions on a given function

def decor1(fun):
    def inner(x):
        result = fun(x)
        return result/2

    return inner


def decor2(fun):
    def inner(x):
        result = fun(x)
        return result**2

    return inner


@decor2 # will be executed second
@decor1 # will be executed first
def num(x):
    return x


print(num(10))
