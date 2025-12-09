arr_list: list[int] = [12, 2, 1, 4, 6, 43]

arr_list_add = [n*2 for n in arr_list if n*2 >= 12]
print(arr_list_add)

arr_list_string: list[str] = ['bonjour', 'bonsoir', 'good', 'name']
arr_list_string_add = [n.upper() for n in arr_list_string if len(n) > 5]
print(arr_list_string_add)


somme = 28
digit = somme % 10
print(digit)
carry = somme // 10
print(carry)


s = "abcabcbb"
print(f"SPLIT : {s.split()}")


print(set('test'))


x = 10
x = x + 10
print(x)


s1 = {"Python", "Java", "c++"}
s2 = {"Python", "Java", "Python"}


s3 = [2, 4, 8, 5, 1]
for num in range(len(s3)):
    print(s3[num])


arr = [4, 3, 2, 7, 8, 2, 3, 1]
k = 0
while k < len(arr):
    print(f"WHILE => {arr[k]}")
    k += 1
