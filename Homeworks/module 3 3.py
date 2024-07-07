def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, 1.0, 'three']
values_dict = {'a': 2, 'b': 4.0, 'c': 'papa'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)


