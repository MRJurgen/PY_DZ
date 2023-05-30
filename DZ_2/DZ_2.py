n = int(input('Введите трехзначное число: '))
third = n%10
n=int(n/10)
second =n%10
first = int(n/10)
print(f'Сумма трех чисел = {first + second + third}')