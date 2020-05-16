'''
Crear un programa  donde le pases un numero, y te devuelva  su tabla de multiplicar
'''
tabla = input("Introduce un numero para obtener su tabla: ")

try:
    tabla = int(tabla)

    #range(X) -> Empieza por 0, y el numero llega hasta X-1

    if(isinstance(tabla, int) and tabla in range(11)): # 0 - 10 tabla in range(11)
        for i in range(11): 
            print(str(tabla) + " x " + str(i) + " = " + str((tabla*i)))
    else:
        print("Solo se permiten numeros del 0 al 10")

except:
    print("Solo se permiten numeros")
