arr_list: list[int] = [12, 2, 1, 4, 6, 43]

arr_list_add = [n*2 for n in arr_list if n*2 >= 12]
print(arr_list_add)

arr_list_string: list[str] = ['bonjour', 'bonsoir', 'good', 'name']
arr_list_string_add = [n.upper() for n in arr_list_string if len(n) > 5]
print(arr_list_string_add)
