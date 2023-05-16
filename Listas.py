# Pedimos al usuario que ingrese el tamaño de la lista
tamaño = int(input("Ingrese el tamaño de la lista de las motos: "))
print("-------------------------------------------------------")
# Creamos las listas vacías
nombres = []
identificaciones = []

# Pedimos al usuario que ingrese los datos de la lista
for i in range(tamaño):
    print("Ingrese los datos de la motocicleta", i + 1)
    nombre = input("Marca: ")
    identificación = input("Placa: ")

    nombres.append(nombre)
    identificaciones.append(identificación)
print("-------------------------------------------------------")
# Mostramos los datos de la lista
for i in range(tamaño):
    print("Mostrando los datos de la moto", i + 1)
    print("Marca:", nombres[i])
    print("Placa:", identificaciones[i])
print("-------------------------------------------------------")
# Búsqueda en la lista
busqueda = input("Ingrese la marca a buscar: ")
encontrado = False

for i in range(tamaño):
    if nombres[i] == busqueda:
        print("Marca:", nombres[i])
        print("Placa:", identificaciones[i])
        encontrado = True
if not encontrado:
    print("No se encontró ningúna marca similar.")
print("-------------------------------------------------------")