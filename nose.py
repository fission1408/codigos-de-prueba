
saldo = 20000000000
lista_ruts_permitidos =["12.345.678-5", "15.987.321-K", "18.456.123-2", "20.111.222-7", "9.876.543-1", "11.222.333-4", "16.789.012-0", "19.555.444-6", "21.000.888-9", "14.333.222-K", "17.654.321-8", "22.444.555-3", "13.999.000-1", "8.123.456-7", "10.888.777-2", "23.555.666-0", "12.000.123-K", "15.432.109-4", "18.777.888-5", "20.654.987-1", "21.121.976-9"] 


lista_permitida = ["sofia", "javier", "elena", "diego", "paula", "andres", "valentina", "ricardo", "isabel", "fernando", "daniela", "hugo", "gabriela", "mateo", "claudia", "sebastian", "marta", "alejandro", "natalia", "pablo", "beatriz", "sergio", "julia", "rodrigo", "laura", "adrian", "victoria", "tomas", "irene", "felipe", "sara", "agustin", "camila", "joaquin", "vicente"]



def validar_nombre(lista_permitida):
    while True:
        nombre = input("Ingrese su nombre: ").lower().strip()
        if nombre in lista_permitida:
            print(f"Bienvenido, {nombre.capitalize()}.")
            return nombre  # El 'return' termina la función y entrega el valor
        else:
            print("Nombre no aceptado. Intente de nuevo.")

def pedir_rut_validado(lista_ruts_permitidos):
    while True:
        # 1. Pedimos el dato
        rut_ingresado = input("Ingresa el RUT (ej: 12.345.678-9): ").strip()
        
        # 2. Primero validamos el formato básico (puntos y guion)
        if len(rut_ingresado) > 7 and "-" in rut_ingresado:
            
            # 3. Ahora validamos si el RUT está en nuestra "base de datos"
            if rut_ingresado in lista_ruts_permitidos:
                print(f"RUT {rut_ingresado} encontrado. Acceso concedido.")
                return rut_ingresado  # Salimos de la función con el RUT válido
            else:
                print(f"Error: El RUT {rut_ingresado} no está registrado en el sistema.")
                # No ponemos return, así el while vuelve a empezar
        
        else:
            print("¡Error! Formato inválido. Asegúrate de incluir puntos y guion.")

# --- EJEMPLO DE USO ---

# Tu "base de datos" de RUTs
ruts_permitidos = ["12.345.678-5", "15.987.321-K", "18.456.123-2","15.432.109-4", "18.777.888-5", "20.654.987-1", "21.121.976-9"]

# Llamamos a la función pasando la lista como argumento
rut_verificado = pedir_rut_validado(ruts_permitidos)

print(f"Sesión iniciada con el RUT: {rut_verificado}")

print("\t ==========Menu=========")
print("1.ingresar dinero a la cuenta")
print("2.retirar dinero de la cuenta")
print("3.mostrar el dinero disponible")

opcion =int(input("elija una opcion del menu"))

if opcion ==1:
   ingreso = float(input("cuanto es el monto a ingresar: "))
   saldo+=ingreso
   print(f"el saldo actual es de (saldo)")
elif opcion ==2:
         retiro= float(input("ingrese el monto a retirar"))
         if retiro>saldo:
            print("saldo insuficiente")
elif opcion ==3:
     print(f"el saldo disponible es de {saldo}")
















input("presione enter para salir")