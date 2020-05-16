# KATA 2: ENTENTDIENDO PYTHON
'''
Una panaderia vende barras de pan a 3.49€ cada una. 
El pan que no es del dia tiene un descuento del 60%.

Ecribre un programa que comience leyendo el número de barras vendidas 
que no son del día. Después tu pograma debe mostrar el precio habitual de una barra de pan,
el descuento  que se le hace por no ser fresca y el coste final total.
'''

precio = 3.49
descuento = 1 - 0.6 #Queda 0,4 que es el porcentaje que queda
precio_con_descuento = precio * descuento

numero_de_barras = input("Introduce el número de barras vendidas: ")
#numero_de_barras = int(numero_de_barras)

print("Precio habitual: " + str(precio))
print("Descuento: " + str(precio_con_descuento))
print("Coste Final: " + str(int(numero_de_barras) * precio_con_descuento))

