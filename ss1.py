print("--------------------------------------")
print("      CALCULADOR DE NOTAS NEM         ")
print("--------------------------------------")

tabla_nem_A = {
    4.0: 100, 4.1: 114, 4.2: 128, 4.3: 142, 4.4: 157, 4.5: 173, 4.6: 189, 4.7: 205, 4.8: 221, 4.9: 238,
    5.0: 256, 5.1: 274, 5.2: 293, 5.3: 312, 5.4: 332, 5.5: 352, 5.6: 374, 5.7: 395, 5.8: 418, 5.9: 441,
    6.0: 466, 6.1: 492, 6.2: 520, 6.3: 549, 6.4: 580, 6.5: 613, 6.6: 649, 6.7: 689, 6.8: 735, 6.9: 791,
    7.0: 1000
}


tabla_nem_BC = {
    4.0: 100, 4.1: 121, 4.2: 142, 4.3: 163, 4.4: 184, 4.5: 205, 4.6: 226, 4.7: 247, 4.8: 268, 4.9: 289,
    5.0: 310, 5.1: 331, 5.2: 352, 5.3: 374, 5.4: 396, 5.5: 418, 5.6: 442, 5.7: 466, 5.8: 491, 5.9: 516,
    6.0: 543, 6.1: 571, 6.2: 601, 6.3: 632, 6.4: 667, 6.5: 704, 6.6: 746, 6.7: 793, 6.8: 847, 6.9: 911,
    7.0: 1000
}

tablas_por_grupo ={
    "A": tabla_nem_A,
    "B": tabla_nem_BC,
    "C": tabla_nem_BC  #ambos grupos apuntan a lo mismo 
    
}

print("\n INTRUCCIONES \n")
print("\n 1.debera escribir cada nota con punto\n ")

#datos del personal
nombre1  = (input("ingrese su primer nombre: ")).lower()

nota1    = float(input("ingrese notas 1ero medio: "))

nota2    = float(input("ingrese notas 2do medio: "))

nota3    = float(input("ingrese notas 3ero medio: "))

nota4    = float(input("ingrese notas 4to medio: "))

promedio = (nota1 + nota2 + nota3 + nota4) /4

print("su promedio es", promedio)

#calculadora nem
print("------------------------------------------------------")
print("              CALCULAR PUNTAJE                        ")
print("\n--------------------------------------------------\n")
print(f"grupo B y C se agrupan")
print("Grupo A: Enseñanza Media Científico-Humanista Diurna")
print("Grupo B: Enseñanza Media Científico-Humanista de Adultos")
print("Grupo C: Enseñanza Media Técnico-Profesional")



def promedio_nem():
    
    grupo = input("Debe ingresar el grupo al que pertenece (A, B, C): ").upper()
    nota_para_la_tabla = round(promedio, 1)
    
    
    if grupo in tablas_por_grupo:
        tabla_seleccionada = tablas_por_grupo[grupo]
        
        if nota_para_la_tabla in tabla_seleccionada:
            puntaje = tabla_seleccionada[nota_para_la_tabla]
            print("\n-------------------------------------------------------\n")
            
            print(f"Estimado/a {nombre1.capitalize()}")
            print(f"Tu puntaje NEM para el Grupo {grupo} es: {puntaje}")
            print("-----------------------------------------------------------")
        else:
            print(f"Error: La nota {nota_para_la_tabla} no está en el rango (4.0 - 7.0).")
    else:
        print("Error: Grupo no válido. Debes ingresar A, B o C.")


promedio_nem()


input("\nPresiona Enter para salir...")