def a():
    c = 0
    def b():
        nonlocal c
        c += 1
        print(c)
    
    b()

a()