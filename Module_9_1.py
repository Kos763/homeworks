def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


def min_list(list):
    return min_list(list)


def max_list(list):
    return max_list(list)


def len_list(list):
    return len(list)


def sum_list(list):
    return sum_list(list)


def sorted_list(list):
    return sorted(list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
