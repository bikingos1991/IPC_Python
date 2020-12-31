def main():
    nombre=input("Escribe tu nombre: ")
    mensaje= "Hola " + nombre +" eres el mej@r."
    print(mensaje)
    print("El mensaje tiene", len(mensaje), "caracteres.")

if __name__ == "__main__":
    main()