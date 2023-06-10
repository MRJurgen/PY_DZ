n=int(input('n : '))
m=int(input('m : '))
k=int(input('k : '))

if(n==1 or m==1 or k==n or k==m or k%2==0 or k%n==0 or k%m==0):
    print('yes')
else:
    print('no')
