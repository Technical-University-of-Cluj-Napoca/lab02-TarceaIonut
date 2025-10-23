def multiply_all(*args:int) -> int:
    res = 1
    for arg in args:
        res *= arg
    return res


#print(multiply_all())