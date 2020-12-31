def main():
    objetivo=int(input("Escoge un numero: "))
    epsilon=0.00001
    bajo=0.0
    alto=max(bajo,objetivo)
    respuesta=(alto+bajo)/2

    while abs(respuesta**2-objetivo)>=epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        
        if respuesta**2<objetivo:
           bajo=respuesta
        else:
            alto=respuesta
        
        respuesta=(alto+bajo)/2
    print(f'La raiz cuadrada aproximada de {objetivo} es {respuesta}')

if __name__ == "__main__":
    main()