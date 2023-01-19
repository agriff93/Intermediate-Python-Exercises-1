my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
def concatDict(dict1, dict2):
    dict3 = dict1 | dict2
    return(dict3)
my_dict_3 = concatDict(my_dict_1, my_dict_2)
print(my_dict_3)