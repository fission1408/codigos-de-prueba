print("============================")
print("    LOGICA 2 CABALLO        ")
print("============================")

caballo = input("eres un caballo? (si/no); ").lower()
if caballo == "no":
    print("entonces no eres un caballo")
if caballo == "si":
     patas = input("en cuantas patas caminas?: ")
if patas == "4":
     print("entonces eres un caballo")
elif patas == "2":
    print("entonces no eres un caballo")
else:
    print("mentiroso no eres un caballo")
    
    
    
input("presione enter para salir: ")
