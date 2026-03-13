# Definimos colores (opcional, pero se ve genial)
CYAN = '\033[36m'
RESET = '\033[0m'

banner_retro = f"""
{CYAN}
  ___________________________________________
 /                                           \\
|    >>>  INICIANDO TERMINAL PYTHON  <<<      |
|           SISTEMA DE VENTAS 2026            |
 \\___________________________________________/
{RESET}
"""

print(banner_retro)

print("---------------------")
print("   CAPTURA DE DATOS  ")
print("---------------------")
nombre = input("escriba su nombre: ")

stock = ["teclado", "mouse", "mousepad", "ssd", "hdd",]
precios = {
    "teclado": 80000,
    "mouse": 50000,
    "mousepad": 15000,
    "ssd": 35000,
    "hdd": 25000
}

print("\n ==== SALDO CUENTA === \n")
saldo  = 345000
print("saldo de cuenta para comprar", saldo)
ver_stock  = input("escriba 'ver' para verificar stock.  ")
if ver_stock == 'ver':
    print("nuestro stock es el siguiente", stock)
elif ver_stock in stock:
    print(f"si, tenemos{ver_stock} disponible.")
else:
    print("producto agotado.")
    

print("\n === PEDIDO ===\n")
pedido = input("que producto desea comprar hoy?: ").lower()
cantidad = int(input(f"cuantas unidades de {pedido} quieres?: "))

print("\n ===carrito de compra===\n")
precio_total = precios[pedido] * cantidad

print("-" * 30)
print(f"subtotal carrito: {precio_total}")

input("presione enter si desea continuar con la compra:")

if saldo >= precio_total:
    saldo = saldo - precio_total
    print(f"compra exitosa {nombre.capitalize()} te quedan {saldo}.")
    

print("-------------------------------")
print("   COMPRA REALIZADA CON EXITO  ")
print("-------------------------------")


















input("presione enter para salir: ")
    



