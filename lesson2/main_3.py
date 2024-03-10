x = 'hello world'
x_split = x.split(' ')
print(x_split)
x_split_2 = x.split('o')
print(x_split_2)
x_join = '-'.join(x_split)
print(x_join)
x_join_2 = '-'.join(x)
print(x_join_2)
new_x = x.replace('w', 'W')
print(new_x)
new_x_2 = x.replace('l', 'L', 2)
print(new_x_2)

# вторую l меняем на L
new_x_3 = x[:3] + x[3:].replace('l', 'L', 1)
print(new_x_3)

count_world = x.count('l')
print(count_world)
index_world = x.index('l')
print(index_world)
find_world = x.find('l')
print(find_world)

print(x[:])
print(x[0:])
print(x[-11::1])
print(x[-11::])
