def howareyou(fun):
    def innerfun(name):
        result = fun(name)
        return result + "\nHow are you?"

    return innerfun


@howareyou
def hello(name):
    return "Hello {}".format(name)


print(hello("Darshan"))
