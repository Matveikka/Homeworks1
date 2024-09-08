def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)
        j = 0
        for i in range(2, sum_ - 1):
            if sum_ % i > 0:
                continue
            if sum_ % i == 0:
                j += 1
        if j > 0:
            print('Составное')
        else:
            print("Простое")
        return result
    return wrapper
@is_prime
def sum_three(*args):
    summa = sum(args)
    return print(summa)
result = sum_three(2, 3, 6)
