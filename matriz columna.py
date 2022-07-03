
fila=[]
cont=0

for x in range(1):
	columna=[]
	for k in range(3):
		cont=cont+1
		columna.append(cont)
		fila.append(columna)

print("-----------------------------")	
print("\nMatriz columna")
print("col| 1  2  3")
print("-----------------------------")
print("fila|")

for x in range(1):
	for k in range(3):
		print("     ",fila[x][k])

