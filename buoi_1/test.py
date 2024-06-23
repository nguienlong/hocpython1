my_list = [{'a': 1}, {'b': 2}, {'c': 3}]
contain_dicts = False
for item in my_list:
    if isinstance(item, dict):
        contain_dicts = True
        break
print(contain_dicts)  # Output: True
