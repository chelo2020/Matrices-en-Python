#Apartir del siguiente algoritmo, podemos cargar los datos de las
#filas y las columnas y asi obtener la matriz que necesitemos.
print("-------------------------------------------------------")
print("                se carga la matriz original            ")

#     0   1   2
#A=  -1   0   3
#    -2  -3   0


matriz=[]
filas=int(input("Cantidad de Filas: "))
columnas=int(input("Cantidad de Columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz [i][j]= int(input("Elemento %d,%d: " % (i,j)))

print("-----------------------------")	
print("\nMatriz Original")
print("col| 1  2  3\nfila|")
print("-----------------------------")


for x in range(filas):
	print("     ",matriz[x])




#Apartir del siguiente algoritmo, podemos cargar los datos de las
#filas y las columnas y asi obtener la matriz que necesitemos.
print("-------------------------------------------------------")
print("                se carga la matriz Antisimetrica            ")


#      0   -1  -2
#At=   1    0  -3
#      2    3   0


matriz=[]
filas=int(input("Cantidad de Filas: "))
columnas=int(input("Cantidad de Columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz [i][j]= int(input("Elemento %d,%d: " % (i,j)))

print("-----------------------------")	
print("\nMatriz Antisimetrica, matriz transpuesta")
print("col| 1  2  3\nfila|")
print("-----------------------------")

for x in range(filas):
	print("     ",matriz[x])