'''
    Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
    triángulo rectángulo como el de más abajo, de altura el número introducido.
    *
    **
    ***
    ****
    *****
'''
lon = int(input("Elige el tamaño del arbol: "))

for i in range(lon): # 1, lon + 1 empieza en 1, el numero del usuario
    print('*' * (i + 1))