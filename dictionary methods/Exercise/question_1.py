my_dict = {}
x = {'name':'john','age':'25','city':'new york'}
my_dict.update(x)
print(my_dict)

my_dict_copy = {}
my_dict_copy  = my_dict.copy()
print(my_dict_copy)

my_dict.pop('age')
print(my_dict)

