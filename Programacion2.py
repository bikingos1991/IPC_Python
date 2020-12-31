def main():
    nombre1=input("Escribe el nombre de la primera persona: ")
    edad1=int(input("Escribe la edad de la primera persona: "))

    nombre2=input("Escribe el nombre de la segunda persona: ")
    edad2=int(input("Escribe la edad de la persona persona: "))

    if edad1>edad2:
        if edad1-edad2==1:
            print(nombre1, " es mayor por ", edad1-edad2 , "año que ", nombre2, ".")
        else:
            print(nombre1, " es mayor por ", edad1-edad2 , "años que ", nombre2, ".")
    elif edad1<edad2:
        if edad2-edad1==1:
            print(nombre1, " es menor por ", edad2-edad1 , "año que ", nombre2, ".")
        else:
            print(nombre1, " es menor por ", edad2-edad1 , "años que ", nombre2, ".")
    else:
        print(nombre1, " y " , nombre2, " tienen  la misma edad, ", edad1 , "años.")

if __name__ == "__main__":
    main()