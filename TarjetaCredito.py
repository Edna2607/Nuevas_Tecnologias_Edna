"""
TARJETA DE CREDTO

1 - Recibir por consola el valor de una compra
2 - que se pueda ingresar el numero de cuotas con las que se va a pagar
3 - Calcular el valor de la cuota
Nota: no calcular intereses
Usando un ciclo While queremos que imprima el plan de pago y le  muestre el cupo liberado con cada pago.

para que genere el plan de pagos : imprimir cuanto paga en cada cuota y cuanto resta del monto inicial """


ValorCompra = int(input("Ingrese el valor Total de la compra = "))
cuota = int(input("Ingrese el numero de cuotas = "))

valor_total = ValorCompra/cuota 
cuota_num = 1

while ValorCompra > 0:
    print("Cuota" , cuota_num, " a pagar = " ,valor_total)
    ValorCompra -= valor_total
    cuota_num += 1
    print("Restante por pagar: " ,ValorCompra)
    
print("Felicitaciones, El Credito ha sido Cancelado!")
