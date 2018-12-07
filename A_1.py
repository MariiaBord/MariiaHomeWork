a=1
b=2
print(a+b)
print('hello world')
list_list_words=['hello','world']
res_count = 0
result_string= ''
while len(list_list_words)>=1:
    res = list_list_words.pop()
    if res:
        result_string += res+','
        print(list_list_words)