print("--------------------------------------------------------")
print("            Matriz cuadrada                             ")    


#Apartir del siguiente algoritmo, podemos cargar los datos de las
#filas y las columnas y asi obtener la matriz que necesitemos.

matriz=[]
filas=int(input("Cantidad de Filas: "))
columnas=int(input("Cantidad de Columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz [i][j]= int(input("Elemento %d,%d: " % (i,j)))



print("-----------------------------")	
print("\nMatriz cuadrada")
print("col| 1  2  3\nfila|")
print("-----------------------------")



for x in range(filas):
	print("     ",matriz[x])