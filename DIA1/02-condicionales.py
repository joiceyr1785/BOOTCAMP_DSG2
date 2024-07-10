#ENTRADA
print("MI CALCULADORA")
numero1 = input("Numero 1 : ")
numero2 = input("Numero 2 : ")
operacion = input("Ingresa el tipo de operación(suma|resta): ")
#PROCESO
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == 'resta'):
    resultado = int(numero1) - int(numero2)
else:
    print("la operacion no existe")
    exit()
#SALIDA
print(f"la operacion {operacion} es {resultado}")
