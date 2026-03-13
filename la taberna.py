CYAN = '\033[36m'
RESET = '\033[0m'

banner_retro = f"""
{CYAN}
  ___________________________________________
 /                                           \\
|    >>>    LA TABERNA DE PYTHON     <<<      |
|                                             |
 \\___________________________________________/
{RESET}
"""
sistema_oro = 100 #oro del jugador inicial

print("=================================")
print("      BIENVENIDO JUGADOR         ")
print("=================================")

usuario = input("escriba un usuario: ")

print("\n ----menu---\n")
print("\n vida,fuerza,magia\n")
menu =["vida, fuerza, magia"]

menu_precios ={
    "vida" : 20,
    "fuerza" : 50,
    "magia" : 70,
}


pociones = input(f"elija una pociones inicial {usuario}: ")
cantidad = int(input(f"cuantas {pociones} deseaa?: "))

# 1. Primero verificamos si lo que escribió está en nuestro diccionario
if pociones in menu_precios:
    # Calculamos el costo total
    total_compra = menu_precios[pociones] * cantidad
    
    print(f"\nEl total por {cantidad} poción(es) de {pociones} es: {total_compra} monedas de oro.")

    # 2. Ahora vemos si el jugador tiene suficiente oro
    if sistema_oro >= total_compra:
        # Si le alcanza, restamos
        sistema_oro = sistema_oro - total_compra
        
        # El Ticket Final
        print(f"""
        ------------------------------------------
        ¡COMPRA EXITOSA, {usuario.upper()}!
        Has adquirido: {cantidad}x {pociones}
        Oro restante: {sistema_oro} monedas.
        ------------------------------------------
        """)
    else:
        # 3. Si NO le alcanza, calculamos cuánto le falta
        falta = total_compra - sistema_oro
        print(f"¡No tienes suficiente oro! Te faltan {falta} monedas.")

else:
    # Si la poción no existe en el diccionario
    print(f"Ese brebaje '{pociones}' no lo vendemos aquí, viajero.")

input("\nPresione Enter para salir de la taberna...")