"""
la aplicacion debe permitir registrar ingresos y contar el saldo de estos.
debe permitir registrar egresos y mostrar el saldo.
si el egreso es mayor que el saldo no debe permitir el retiro y mostrará un mensaje de saldo insuficiente.
la aplicacion llevara registro de los movimientos indicando el numero de ingresos y de egresos
Debe registrar ingresos y egresos.
si los ingresos son mayor que el saldo, debe indicar que no tiene saldo suficiente y dejar el mismo saldo, no puede mostrar saldo negativo, debe contar cuantos ingresos se han dado y cuantos egresos """

saldo = 0
acumIngresos = 0
acumEgresos = 0

isOn = int(input("Ingrese 1 para inicializar el servicio: "))

while isOn != 0:
    opc = int(input("1.Ingreso: \n2.Egreso: \n3.Salir \nResultado = "))

    print("******************************************************")

#------------------------------------------------------------------
#OPCION 1
    if opc == 1:
       ingreso = int(input("Registre el ingreso: "))

       saldo = saldo + ingreso
       print(f"Su Saldo es ${saldo} ")

       acumIngresos+=1
       print(acumIngresos)
  
#----------------------------------------------------------------
#OPCION 2
    elif opc==2:
       egreso = int(input("Registre el monto a retirar: "))
    
       saldo = saldo - egreso

       if saldo < 0:
         print("Saldo Insuficiente")
         saldo = saldo + egreso
         print(saldo)

       else:
         print(f"Su Saldo es: ${saldo}")
         acumEgresos += 1
         print(acumEgresos)

#--------------------------------------------------------------
#OPCION 3
    elif opc == 3:
       print("Salir de la aplicacion ")
       isOn=0

    else:
       print("Ingrese una opcion valida")
       
        
      