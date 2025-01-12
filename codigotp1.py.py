cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))
inicial = 0
provincia = "No aplica"
destino = None
cp_length = len(cp)
region = None
uru = None
if cp[-1].isdigit():
    if cp_length == 4 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit():
        destino = "Bolivia"
    elif cp_length == 6 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit() and cp[-6].isdigit():
        destino = "Paraguay"
    elif cp_length == 5 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit():
        destino = "Uruguay"
        if cp[0] == "1":
            uru = "Uruguay (Montevideo)"
        else:
            uru = "Uruguay (No Montevideo)"
    elif cp_length == 7 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit() and cp[-6].isdigit():
        destino = "Chile"
    elif cp_length == 9 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4] == "-" and cp[-5].isdigit() and cp[-6].isdigit() and cp[-8].isdigit() and cp[-9].isdigit():
        destino = "Brasil"
        if cp[0] == "1":
            region = 1
        elif cp[0] == "2":
            region = "2"
        elif cp[0] == "3":
            region = 3
        elif cp[0] == "4":
            region = 4
        elif cp[0] == "5":
            region = 5
        elif cp[0] == "6":
            region = 6


        elif cp[0] == "7":
            region = 7
        elif cp[0] == "8":
            region = 8
        elif cp[0] == "9":
            region = 9
        else:
            region = 0
    else:
        destino = "Otro"
elif cp[-1].isalpha() and cp[-2].isalpha() and cp[-3].isalpha() and cp[-4].isdigit() and cp[-5].isdigit() and  cp[-6].isdigit() and cp[-7].isdigit() and cp[-8].isalpha() and cp[0] != "I" and cp[0] != "Ñ" and cp[0] != "O":
    destino = "Argentina"
    if cp[0] == "A":
        provincia = "Salta"
    elif cp[0] == "B":
        provincia = "Provincia de Buenos Aires"
    elif cp[0] == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif cp[0] == "D":
        provincia = "San Luis"
    elif cp[0] == "E":
        provincia = "Entre Ríos"
    elif cp[0] == "F":
        provincia = "La rioja"
    elif cp[0] == "G":
        provincia = "Santiago del Estero"
    elif cp[0] == "H":
        provincia = "Chaco"
    elif cp[0] == "J":
        provincia = "San Juan"
    elif cp[0] == "K":
        provincia = "Catamarca"
    elif cp[0] == "L":
        provincia = "La Pampa"
    elif cp[0] == "M":
        provincia = "Mendoza"
    elif cp[0] == "N":
        provincia = "Misiones"
    elif cp[0] == "P":
        provincia = "Formosa"
    elif cp[0] == "Q":
        provincia = "Neuquén"
    elif cp[0] == "R":
        provincia = "Rio negro"
    elif cp[0] == "S":
        provincia = "Santa Fe"
    elif cp[0] == "T":
        provincia = "Tucuman"
    elif cp[0] == "U":
        provincia = "Chubut"
    elif cp[0] == "V":
        provincia = "Tierra del Fuego"
    elif cp[0] == "W":
        provincia = "Corrientes"
    elif cp[0] == "X":
        provincia = "Cordoba"
    elif cp[0] == "Y":
        provincia = "Jujuy"
    elif cp[0] == "Z":
        provincia = "Santa cruz"

else:
    destino = "Otro"


if tipo == 0:
    inicial = 1100
elif tipo == 1:
    inicial = 1800
elif tipo == 2:
    inicial = 2450
elif tipo == 3:
    inicial = 8300
elif tipo == 4:
    inicial = 10900
elif tipo == 5:
    inicial = 14300
elif tipo == 6:
    inicial = 17900


final = 0

if pago == 1 and destino == "Argentina":
    final = inicial - ((inicial * 10) / 100)
else:
    final = inicial
if destino == "Bolivia" or destino == "Paraguay" or uru == "Uruguay (Montevideo)":
    inicial = inicial + ((inicial * 20) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial
elif destino == "Chile" or uru == "Uruguay (No Montevideo)":
    inicial = inicial + ((inicial * 25) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial
elif region == 8 or region == 9:
    inicial = inicial + ((inicial * 20) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial
elif region == 0 or region == 1 or region == 2 or region == 3:
    inicial = inicial + ((inicial * 25) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial

elif region == 4 or region == 5 or region == 6 or region == 7:
    inicial = inicial + ((inicial * 30) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial
elif destino == "Otro":
    inicial = inicial + ((inicial * 50) / 100)
    if pago == 1:
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial

inicial = int(inicial)
final = int(final)

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)