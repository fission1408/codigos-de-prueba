print("=======================================")
print("       CALCULADORA DE NOTAS            ")
print("=======================================")

#ingresar notas 
nombre = input("ingrese su nombre: ").lower()
nota1 = float(input("ingresar nota de su 1er semestre: "))
nota2 = float(input("ingresar nota de su 2do semestre: "))
nota3 = float(input("ingresar nota de su 3er semestre: "))
nota4 = float(input("ingresar nota de su 4to semestre: "))

promedio = round(nota1 + nota2 + nota3 + nota4) /4

print("su nota es", promedio)

if promedio >= 6.8:
    print("felicitaciones su nota es", promedio)
elif promedio >= 4.0:
 print("buen trabajo su promedio es", promedio) 
elif promedio <= 4.0:
 print("reprobado")

else:
    print("reprobado")
    






input("apriete enter para salir: ")
 