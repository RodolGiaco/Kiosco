import kiosko_app as funcion

print("-------BIENVENIDO AL KIOSCO ROLFI-------")
menu = """========MENU=======
1) Agregar producto
2) Ver producto 
3) Eliminar producto
4) Salir"""
while True:
    print(menu)
    opcion = int(input(">>>"))
    

    if opcion == 1:
        funcion.agregar()
    elif opcion == 2:
        funcion.ver()
    elif opcion == 3:
        funcion.eliminar()
    elif opcion == 4:
        print("Adios gracias por tu visita")
        break
    
    else:
        print("Opcion incorrecta")
