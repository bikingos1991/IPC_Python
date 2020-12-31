def main():
    objetivo=int(input("Escoge un numero: "))
    epsilon=0.01
    paso  = epsilon**2
    respuesta=0.0

    while abs(respuesta**2-objetivo)>=epsilon and respuesta<=objetivo:
        respuesta += paso
        #print(abs(respuesta**2-objetivo), respuesta)
        

    if abs(respuesta**2-objetivo)>=epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'a raiz cuadrada de {objetivo}  es  {respuesta}')

if __name__ == "__main__":
    main()