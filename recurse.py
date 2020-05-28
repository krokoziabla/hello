def foo():
    a = input()
    if a != "0":
        foo()
    print(a, " ")

foo()
