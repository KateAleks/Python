number = input ('Введите число ')
print (number)
sum=0
for i in number:
    if i.isdigit():
        sum += int(i)
      # print(f'Сумма введенных элементов числа =  {sum}')
        print (f'Сумма цифр числа = {sum}')