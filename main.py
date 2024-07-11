

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['522', 949, (1, 2, 3)]
values_dict = {'a': 'Строка', 'b': 9.58, 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)
