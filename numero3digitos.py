numero = int(input("Ingrese un número de 3 digitos : "))
uni = numero % 10
decena = numero // 10
aux1= numero % 100
uni2 = aux1 % 10 
decena2 = aux1 // 10
cente = numero // 100
unidad = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
decimal = ["","dieci","veinti","trenta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
especiales = ["","once", "doce","trece","catorce","quince"]
centena = ["","ciento","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
if numero > 0 and numero < 100:
    if numero > 0 and numero <= 9:
        print(unidad[uni])
    elif numero == 10:
        print("diez")
    elif numero > 10 and numero <= 15:
        print(especiales[uni])
    elif (numero >= 16 and numero <= 29) and (uni != 0):
        print(decimal[decena]+unidad[uni])
    elif numero == 20:
        print("veninte")
    elif (numero >= 30 and numero <= 99) and (uni != 0):
        print(decimal[decena]+" y "+unidad[uni])
    elif (numero >= 30 and numero <= 99) and (uni == 0):
        print(decimal[decena])
elif numero > 99 and numero < 1000:
    if numero == 100:    
        print("cien")
    elif numero > 100 and numero <= 109:
        print(centena[cente]+unidad[uni2])
    elif numero == 110:
        print(centena[cente]+"diez")
    elif numero > 110 and numero <= 115:
        print(centena[cente]+especiales[uni2])
    elif (numero >= 116 and numero <= 129) and (uni != 0):
        print(centena[cente]+decimal[decena2]+unidad[uni2])
    elif numero == 120:
        print(centena[aux]+"veninte")
    elif (numero >= 130 and numero <= 999) and (uni != 0):
        print(centena[cente]+decimal[decena2]+" y "+unidad[uni2])
    elif (numero >= 130 and numero <= 999) and (uni == 0):
        print(centena[cente]+decimal[decena2])
        
else :
    print ("Ingrese un número valido")