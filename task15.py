number = int(input ('Введите число  '))
my_list = []
multipl = 1
for i in range(1,number +1):
    multipl*=i
    my_list.append(multipl) 
    print(f'Результат умножения всех элементов списка = {my_list}')