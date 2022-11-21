#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input ('Введите число  '))
my_list = []
multipl = 1
for i in range(1,number +1):
    multipl*=i
    my_list.append(multipl) 
    print(f'Результат умножения всех элементов списка = {my_list}')
