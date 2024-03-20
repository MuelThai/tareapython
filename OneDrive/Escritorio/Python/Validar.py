while True :
    entrada = input("Ingrese un numero entero: ")

    if entrada.isdigit():
        numero = int(entrada)

        print(f"Ha ingresado el numero entero: {numero}")
        break
    else:
        print("Por favor ingrese solo numeros enteros")