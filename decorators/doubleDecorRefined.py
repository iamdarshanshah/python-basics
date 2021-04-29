# Using @Decorator for applying decorator to a normal function

def decorFun(fun):
    def innerFun():
        result = fun() * 2
        return result

    return innerFun


@decorFun  # applying decorator to num function
def num():
    return 5


print(num())  # 10
