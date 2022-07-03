
#Apartir del siguiente algoritmo, podemos cargar los datos de las
#filas y las columnas y asi obtener la matriz que necesitemos.
print("-------------------------------------------------------")
print("                se carga la matriz original            ")

#     1  -2  -3
#A=   2   1   0
#     3   0   1


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
print("                se carga la matriz Asimetrica            ")


#      1   2  3
#At=  -2   1  0
#     -3   0  1


matriz=[]
filas=int(input("Cantidad de Filas: "))
columnas=int(input("Cantidad de Columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz [i][j]= int(input("Elemento %d,%d: " % (i,j)))



print("-----------------------------")	
print("\nMatriz Asimetrica, matriz transpuesta")
print("col| 1  2  3\nfila|")
print("-----------------------------")



for x in range(filas):
	print("     ",matriz[x])






