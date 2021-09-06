
def main():
    #Escribe tu código debajo de esta línea
    def triangulo(x):
    for i in range (x,-1,-1):
        for j in range (0,i,1):
            print('*',end="")
    print("")

    for i in range (x,-1,-1):
        for j in range (i):
            print(" ",end="")
    for k in range (i,x):
        print('*',end="")
    print("")
x=int(input('Introduce un número:'))
triangulo(x)
    pass


if __name__=='__main__':
    main()
