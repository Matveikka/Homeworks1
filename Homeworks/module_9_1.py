def _min(int_list):
    return min(int_list)
def _max(int_list):
    return max(int_list)
def _len(int_list):
    return len(int_list)
def _sum(int_list):
    return sum(int_list)
def _sorted(int_list):
    return sorted(int_list)
def apply_all_func(int_list: list, *functions):
    result_d: dict = {}
    for f in functions:
        result = f(int_list)
        result_d[f.__name__] = result
    return result_d
print(apply_all_func([6, 20, 15, 9], _max, _min))
print(apply_all_func([6, 20, 15, 9], _len, _sum, _sorted))





