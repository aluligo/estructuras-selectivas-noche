#Estructura simple
a = 33
b = 200

if b > a:
    print(b, "Es mayor que ",a)

#Estructura Doble

if a > b:
    print(a, "Es mayor que ",b)
else:
    print(a, "No es  mayor que ",b)

#Estructura Multiple
c = 200
d = 207

if c > d:
    print(c,"es mayor que ",d)
elif c < d:
    print(c,"es menor que ",d)
else:
    print(a,"es igual que ",b)

#Estructura enlazada

x = 28

if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")

    else:
        print("pero no por encima de 20.")

#Parametro END

print("Estudiar los sabados",end=' ')# evita el salto de linea y se puede completar con texto dentro de las comillas

print("es genial")

#Parametro SEP

print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila", sep="")#Quita el espacio
print("Daniela","Luis","Carlos","Camila", sep=",")#Agrega una coma

print("Daniela","Luis","Carlos","Camila", sep="_", end="_Curso_Python")

