#Cargar una matriz de 4x3 elementos ( M(4,3) ) 
# por filas.
matriz=[]
filas=int(input("Cantidad de Filas: "))
columnas=int(input("Cantidad de Columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz [i][j]= int(input("Elemento %d,%d: " % (i,j)))



print("-----------------------------")	
print("\nMatriz Asimétrica")
print("col| 1  2  3\nfila|")
print("-----------------------------")



for x in range(filas):
	print("     ",matriz[x])






