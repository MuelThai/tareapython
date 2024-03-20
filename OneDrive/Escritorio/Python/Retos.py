numero = input ("Ingrese un numero: ")

numero = int (numero)

multiplo5 = numero % 5 == 0 

if multiplo5 :
    print(f"{numero} es multiplo de 5.")
elif multiplo5:
    print(f"{numero} no es multiplo de 5. ")
