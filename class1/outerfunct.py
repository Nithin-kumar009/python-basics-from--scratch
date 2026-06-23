def outer():
    def inner():
        print("innner function")
    return inner

result=outer()
result()
print(result)
print(type(result))
