def main():
    #escribe tu código abajo de esta línea
    n=int(input('Inserte la cantidad de símbolos a repetir:'))
for numero in range(n):
    if numero%2 == 0:
        print('#')

    else:
        print('%')
    pass

if __name__=='__main__':   
    main()
