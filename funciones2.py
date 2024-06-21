import time
import os
import csv

bus = [["O" for x in range(4)] for y in range(7)]
precio_boleto = 10000

ventas = []


def menu_bus_y_opciones(p_opcs):
    while True:
        print('Menú Tur-Bus\n\t1. Asientos disponibles\n\t2. Comprar asientos\n\t3. Venta realizadas\n\t4. Generar archivo csv ventas\n\t5. Salir\n')
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print('ERROR! debe ingresar una opcion valida, opciones valida (1,2,3,4,5)!')
            limpiar_pantalla_esperar()
        except:
            print('ERROR! debe ingresar un número entero!')
            
def mostrar_asientosdisp():
    while True:
        print('Frente del Bus')
        print('_________________')
        for f in bus:
            print(f)
        try:
            opc_salir = int(input('¿Deseas salir? Ingrese (1:Salir 0:Redirigir): '))
            if opc_salir in (1,0):
                if opc_salir == 1:
                    print('saliendo')
                    limpiar_pantalla_esperar()
                    break
                else:
                    print('Redirigiendo.')
                limpiar_pantalla_esperar()
        except:
            print('ERROR! debe ingresar un número entero!')

def comprar_asiento():
        print('Frente del Bus')
        print('_________________')
        for f in bus:
            print(f)
        while True:
            try:
                fila_asiento = int(input('Ingrese la fila del asiento (1,2,3,4,5,7): '))
                if fila_asiento in (1,2,3,4,5,6,7):
                    print(f'fila escogida: {fila_asiento}!')
                    break
                else:
                    print('ERROR! debe ingresar una fila valida, filas validas(1,2,3,4,5,6,7)!')
            except:
                print('ERROR! debe ingresar un numero entero!')
        while True:
            try:
                columna_asiento = int(input('Ingrese la posicion del asiento(1,2,3,4): '))
                if columna_asiento in (1,2,3,4):
                    print(f'Posicion escogida: {columna_asiento}!')
                    break
                else:
                    print('ERROR! debe ingresar una posición valida, posiciones valida(1,2,3,4)!')
            except:
                print('ERROR! debe ingresar un numero entero!')
        limpiar_pantalla_esperar()

        
        while True:
            if bus[fila_asiento-1][columna_asiento-1] == "O":
                bus[fila_asiento-1][columna_asiento-1]="X"
                break
            else:
                if bus[fila_asiento-1][columna_asiento-1] == "X":
                    print('EL ASIENTO NO ESTA DISPONIBLE!')
                    continue

        while True:
            print('Registrar datos pasajero!')
            limpiar_pantalla_esperar()

            nombre_pasajero = str(input('Ingrese su nombre: '))
            if len(nombre_pasajero.strip()) >= 3:
                print('Nombre registrado!')
                limpiar_pantalla_esperar()
                break
            else:
                print('ERROR! debe ingresar un nombre que contenga al menos 3 letras!')
            limpiar_pantalla_esperar()

        while True:
            try:
                edad_pasajero = int(input('Ingrese su edad: '))
                if edad_pasajero >= 1 and edad_pasajero <= 130:
                    print('Edad registrada!')
                    limpiar_pantalla_esperar()
                    break
                else:
                    print('ERROR! debe ingresar una edad valida, la edad debe estar dentro del rango de años 1 a 130 años!')
                limpiar_pantalla_esperar()
            except:
                print('ERROR! debe ingresar un número entero!')

        while True:
            try:
                num_telefono = int(input('Ingrese su numero celular: '))
                if len(str(num_telefono)) == 9:
                    print('Numero celular registrado!')
                    limpiar_pantalla_esperar()
                    break
                else:
                    print('ERROR! debe ingresar numero que contenga al menos 9 digitos y el primer numero sea 9!')
                limpiar_pantalla_esperar()
            except:
                print('ERROR! debe ingresar números enteros!')

        if edad_pasajero < 18:
            valor_pasaje = round(precio_boleto * 0.20,)
            print('Recibes un "20%" de descuento por ser menor de 18 años!')
            limpiar_pantalla_esperar()
        elif edad_pasajero > 65:
            valor_pasaje = round(precio_boleto * 0.15)
            print('Recibes un "15%" de descuento por ser mayor de 65 años!')
            limpiar_pantalla_esperar()
        else:
            valor_pasaje = precio_boleto

        pasaje_persona = [fila_asiento-1,columna_asiento-1,nombre_pasajero,edad_pasajero,num_telefono,valor_pasaje]
        ventas.append(pasaje_persona)
        print('BOLETO REGISTRADO!')
        






def ventas_realizadas():
    print('VENTAS TURBUS')
    limpiar_pantalla_esperar
    if len(ventas) >= 1:
        while True:
            print('VENTAS REALIZADAS')
            print('____________________')
            for x in ventas:
                print(f'Asiento fila:\n\t{x[0]}\n\t Posicion asiento:\n\t{x[1]}\n\t Nombre pasajero:\n\t{x[2]}\n\t edad pasajero\n\t{x[3]}\n\t telefono: \n\t{x[4]}\n\t valor pasaje: \n\t{x[5]}\n\t')
            try:
                opc_salirventas = int(input('¿Deseas salir? Ingresa (1: Salir 0: Redirigir): '))
                if opc_salirventas in (1,0):
                    if opc_salirventas == 1:
                        print('Saliendo.')
                        limpiar_pantalla_esperar()
                        break
                    else:
                        print('Redirigiendo')
                    limpiar_pantalla_esperar()
                else:
                    print('ERROR! debe ingresar una opcion valida, opciones validas(1 o 0)!')
                limpiar_pantalla_esperar()
            except:
                print('ERROR! debe ingresar un numero entero')
    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_pantalla_esperar()
def generar_archivo_csv():

    if len(ventas) >= 1:
        nombre_archivo = str(input('ingrese el nombre del archivo: '))
        try:
            with open(f"{nombre_archivo}.csv","x",newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(ventas)
            print('ARCHIVO CREADO!')
        except:
            print('EL NOMBRE DEL ARCHIVO YA SE ENCUENTRA REGISTRADO!')
    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_pantalla_esperar()
    
    

def salir():
    for x in range(1,4):
        print('Saliendo de la app tur-bus',("."*x))
        limpiar_pantalla_esperar()

    












def limpiar_pantalla_esperar():
    time.sleep(1)
    os.system('cls')

