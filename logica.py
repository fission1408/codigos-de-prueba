print("==============================")
print("  EJEMPLO DIAGRAMA DE FLUJO   ")
print("==============================")

feliz = input(" eres feliz? (si/no): ").lower()
if feliz == "si" :
    print("sigue asi,es muy importante ser feliz")
    
    
elif feliz == "no" :
    print("no te preocupes, a veces es normal pero mañana es nuevo dia para  ser feliz")
    quiere_ser_feliz = input("quieres ser feliz? (si/no): ").lower()
    
    if quiere_ser_feliz == "si":
        print("entonces, intenta buscar cosas que te hagan sentir bien")
    elif quiere_ser_feliz == "no":
        print("esta bien, pero recuerda que siempre puedes cambiar")
    else:
        print("respuesta no valida, porfavor responda con solo si o no")
        
else:
    print("respuesta no valida, porfavor responda con solo si o no")


input("presione enter para salir: ")
