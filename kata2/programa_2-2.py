'''
Escribrir un programa que almacene la cadena de caracteres contraseña en una variable.
, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada 
sin tener en cuenta mayusculas y minúsculas.
'''

password = "contraseña"

password_del_usuario = input("Introduzca una contraseña: ").lower() 
#password_del_usuario = password_del_usuario.lower() #para no tener en cuenta las mayusculas, se convierte en minusculas

if password == password_del_usuario:
    print("El password es correcto")
else:
    print("El password no coincide")