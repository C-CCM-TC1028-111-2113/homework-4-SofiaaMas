def main():
    #escribe tu código abajo de esta línea
contador=0
suma=0
numero=1

while True:
    numero=float(input('Inserte un número (número negativo para terminar):'))
   
    if numero <0:
        break

    suma+=numero
    contador+=1

    if contador == 0:
        print('No digitó ningun número')
    
    else:
        promedio=suma/contador

print('El promedio de los es:',promedio)
    pass
if __name__=='__main__':
    main()
