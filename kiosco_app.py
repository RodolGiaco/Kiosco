from prettytable import PrettyTable


stock = [
            {   "id":1,
                "nombre":"Aguila",
                "cantidad":200,
                "precio_u":100.0   }, 

            {   "id":2,
                "nombre":"Tatin",
                "cantidad":150,
                "precio_u":80.0    }, 

            {   "id":3,
                "nombre":"Entre dos",
                "cantidad":500,
                "precio_u":150.0,  }, 

            {   "id":4,
                "nombre":"Guaymallen",
                "cantidad":1500,
                "precio_u":60.0    }, 

            {   "id":5,
                "nombre":"Milka",
                "cantidad":250,
                "precio_u":120.0   }
                                      ]
encabezado_stock = ["id","nombre","cantidad","precio_u"]
encabezado_carrito=["producto","id","nombre","cantidad","precio_u","precio_c"    ]
carrito = []
                              
def agregar():
    print("Elegir un producto de la lista para AGREGAR")
    ver(stock,encabezado_stock)
    ID = int(input("Ingresar N° de producto \n>>>"))
    cantidad = int(input("Cantidad >>"))
    productoAgregar = {   "producto": len(carrito)+1,
                          "id": ID,
                          "nombre": stock[ID-1]["nombre"],
                          "cantidad": cantidad,
                          "precio_u": stock[ID-1]["precio_u"],
                          "precio_c": cantidad*stock[ID-1]["precio_u"]
                      } 
    actualizar(ID,cantidad)    
    carrito.append(productoAgregar)
    ver(carrito,encabezado_carrito)
    print("Agregando producto...")
    

def ver(lista_productos=carrito,encabezados = encabezado_carrito): #por defecto si no le paso nada toma estos valores
    if len(lista_productos)>0:
        tabla = PrettyTable()
        tabla.field_names = encabezados
        for alfajor in lista_productos:
            tabla.add_row(alfajor.values())
        print(tabla)
    else:
        print("No hay productos")


def actualizar(ID,cantidad):
    for diccionario in stock:
        for clave in diccionario.values():
            if clave == ID:
                diccionario["cantidad"] -= cantidad


def eliminar():
    ver(carrito,encabezado_carrito)
    print("Elegir un producto de la lista para ELIMINAR")
    producto = int(input(">>>"))
    productoEliminar = carrito.pop(producto-1) 
    numProducto = productoEliminar["producto"]
    for alfajores in carrito[producto-1:]: #El comienzo es el mismo lugar donde se encontraba el que borramos
        alfajores["producto"] = numProducto
        numProducto += 1
    print("Eliminando el producto")

   

    
    

    


    
