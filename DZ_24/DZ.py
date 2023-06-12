from random import randint

bush = open('bush.txt')
bush = int(bush.readline())
bushes = {}

for item in range(20):   #0-19
    bushes[item] = randint(20,150)

qual_berry = bushes[bush] + bushes[bush+1] + bushes[bush-1] 


print(f'Максимально собрать ягод можно : {qual_berry}')