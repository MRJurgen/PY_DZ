numberA=int(input('Первое число для сложения : '))
numberB=int(input('Второе число для сложения : '))

def sum(a, b):
    if (b==0):
        return a
    elif(b<0):
        return sum(a-1,b+1)
    return sum(a+1,b-1)

print(f"Ответ: {sum(numberA,numberB)}")