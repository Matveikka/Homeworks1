def divide(first, second):
    if second == 0:
        from math import inf
        return inf
    else:
        a = first / second
        print(a)
divide(10,0)