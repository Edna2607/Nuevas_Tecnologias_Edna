
# Variables globales para almacenar los datos de registro
NumeroTarjeta = 0
usuarios = []
prestamos_bicis = []

# ------- FORMULARIO DE REGISTRO --------
def registro():
      print("------- Formulario de Registro ----------- ")
      nombre = input("Ingrese su nombre = ")
      email = input("¿Ingrese su email? = ")
      contraseña = input("Ingrese su contraseña = ")
      NumeroTarjeta = input("¿Ingrese su numero de Tarjeta ? = ")
      usuario = ["nombre = " +nombre+ " - # de Tarjeta = " +NumeroTarjeta+ " - Contraseña : " +contraseña+ " - email: " +email] #Aqui se guarda la informacion del usuario
      usuarios.append(usuario)


def alquiler():
        NumTarjeta = int(input(" INGRESA - Numero de La tarjeta =  "))
        registro_usuario = usuarios[1 == NumTarjeta]
       

        if registro_usuario:
            origen = input("¿Ingrese su Origen? = ")
            destino = input("Ingrese el Destino = ")
            print(" ------ Inicio de sesión exitoso. ----------")
            print("El origen y el destino esta Autorizado ")
            print("--- Bicicleta Disponible para prestamo----")

            viaje=["Origen: "+origen+ " - Destino: "+destino]
            prestamos_bicis.append(viaje)
        
        else:
            print(" ------- Inicio de sesión fallido o no se ha registrado. ----------------- ")



# Bucle principal
while True:
    print(" ----------- Seleccione una opción: --------------")
    print("1. Registro")
    print("2. Prestamo de Bicicleta")
    print("3. Salir")
    
    opcion = input("Ingrese el número de opción =  ")

    if opcion == "1":
       registro()
    elif opcion == "2":
       alquiler()      
    elif opcion == "3":
         print(" ---- Saliendo del programa.------ ")
         break
    else:
         print("Opción inválida. Seleccione una opción válida.") 

print("\nLista de bicicletas prestadas:")
for viaje in prestamos_bicis:
    print("Informacion del usuario : " ,usuarios[:2])
    print("Origen:", viaje)
    
  



