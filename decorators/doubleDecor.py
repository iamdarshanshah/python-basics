# Decorator that doubles the result of a function

def decor(fun):
    def innerFun():
        result = fun()
        return result * 2

    return innerFun


def num():
    return 5


resultDecorfun = decor(num)

print(resultDecorfun())  # 10
