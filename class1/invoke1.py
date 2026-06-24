def outer():
    print("outer function started")
    def inner():
        print("inner function")
    return inner
inner=outer()
inner()