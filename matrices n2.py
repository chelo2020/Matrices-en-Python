#Con los datos ingresados del ejercicio anterior
# ,sumar los valores y 
# determinar la  posición del número mayor.
vector=[]
x=0
suma=0

for x in range(10):
    elementos=int(input("Ingresar los elementos al vecto: "))
    vector.append(elementos)
    suma=suma+elementos
    

mayor=vector[0]
posicion=0

for x in range(1,10):
    if vector[x]>mayor:
        mayor=vector[x]
        posicion=x

print("el mayor de los vectores es: ",mayor)
print("su posicion: ",posicion)

