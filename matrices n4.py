#Generar una matriz de 5 filas y 7 columnas, 
# sumar los valores de las filas y los valores
#  de las columnas. 
matriz=[]

filas=int(input("Cantidad de filas: "))
columnas=int(input("Cantidad de columnas: "))

for i in range(filas):
    matriz.append([0]*columnas)
cont=0
for j in range(filas):
    for k in range(columnas):
        matriz[j][k]=int(input("Elemento %d,%d"%(j,k)))
    cont=cont+matriz[j][k]

cont1=0
for k in range(columnas):
    for j in range(filas):
        cont1=cont1+matriz[k][j]

        
print(matriz)
print(cont)
print(cont1)

    




