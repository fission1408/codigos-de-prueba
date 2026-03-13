print("------------menu de compras----------------")
print("1.           coco_cola                 $800")
print("2.           fanta                     $700")
print("3.           sprite                    $750")
print("          ELIJA UNA OPCION                 ")
print("===========================================")

opcion = int(input("ingrese el numero de la opcion que desea comprar: "))
if opcion == 1:
    print("usted ha seleccionado coco_cola, el valor a pagar es de $800")
elif opcion == 2:
    print("usted ha seleccionado fanta, el valor a pagar es de $700")
elif opcion == 3:
    print("usted ha seleccionado sprite, el valor a pagar es de $750")
else:
    print("ingrese una opcion valida")

cantidad = int(input("ingrese la cantidad de unidades de que desea comprar: "))

if cantidad > 0:
    if opcion == 1:
        total = cantidad * 800
        print(f"el total a pagar por {cantidad} unidades de coco_cola es de ${total}")
    elif opcion == 2:
        total = cantidad * 700
        print(f"el total a pagar por {cantidad} unidades de fanta es de ${total}")
    elif opcion == 3:
        total = cantidad * 750
        print(f"el total a pagar por {cantidad} unidades de sprite es de ${total}")
    else:
        print("ingrese una opcion valida")
print("===============================================")
print("        BOLETA    DE COMPRA                    ")
print(f"producto seleccionado:{opcion}                ")
print(f"cantidad: {cantidad}                          ")
print(f"total a pagar: ${total}                       ")
print("===============================================")

input("presione enter para salir")
