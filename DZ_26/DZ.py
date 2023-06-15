
number=int(input('Число для возведения в степень : '))
degree=int(input('В какую степень возвести : '))

def value(number, degree):
    if (degree==0):
        return 1
    return number * value(number,degree-1)

print(f"Ответ: {value(number,degree)}")

