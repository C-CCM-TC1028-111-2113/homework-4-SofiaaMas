
def main():
    #escribe tu código abajo de esta línea
    a=0
b=1
c=0
while True:
    n=(int(input('Inserte un número >=0:')))
    if n>=0:
        break
print('0',end=' ')
for i in range(1,n):
    c=a+b
    print(f"{c}",end=' ')
    a=b
    b=c
print('')
    pass

if __name__=='__main__':
    main()
