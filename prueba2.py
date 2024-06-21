from funciones2 import *

print('Bienvenido a la app tur-bus!')
limpiar_pantalla_esperar()

opciones = (1,2,3,4,5)


while True:
    opc = menu_bus_y_opciones((opciones))

    if opc == 1:
        print('Asientos disponibles!')
        limpiar_pantalla_esperar()
        mostrar_asientosdisp()
       
    elif opc ==2:
        print('Comprar asientos!')
        limpiar_pantalla_esperar()
        comprar_asiento()
    elif opc == 3:
        print('Ventas!')
        limpiar_pantalla_esperar()
        ventas_realizadas()
    elif opc == 4:
        print('Crear archivo de ventas con csv!')
        limpiar_pantalla_esperar()
        generar_archivo_csv()
    else:
        salir()
        break

