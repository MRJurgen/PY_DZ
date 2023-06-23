

phrases = input('Введите фразу : ')

phrases = phrases.lower()
# print(phrases)
phrases = phrases.split()
# print(phrases)
my_dict = {}
vowels = ('уеыаоэёяию')

for i in range(len(phrases)):
    kol = 0
    for j in range(len(phrases[i])): 
        for k in range(len(vowels)):    
            if (phrases[i][j] == vowels[k]):
                kol+=1
    # print({phrases[i], kol})
    my_dict[phrases[i]]= kol

answer = True
for x in my_dict:
    for y in my_dict:
        if(my_dict.get(x)!=my_dict.get(y)):
            answer = False
            
if(answer):
    print('Парам пам-пам')
else:
    print('Пам парам')

