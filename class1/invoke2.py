def outer():
    print("outer function started")
    def inner():
        print("inner function")
    return inner() #type error because we can return on the reference not the function
inner=outer()
inner()