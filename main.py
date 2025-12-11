import oracledb
from api.time_api import *
from bd_crud.crud_carrito import insertar_carrito
from bd_crud.crud_clientes import *
from bd_crud.crud_producto import *
from clases import clase_carrito as carrito_module
from clases import clase_cliente as cliente_module
from clases import clase_producto as producto_module
import time
 


#--------------------creacion de productos----------------------------
#creamos productos
p1 = producto_module.producto(1, "Café", 2500)
p2 = producto_module.producto(2, "Pan", 1000)
p3 = producto_module.producto(3, "te", 500)
#insertamos productos en la base de datos
insertar_producto(p1.codigo, p1.nombre, p1.precio_neto, "activo")
insertar_producto(p2.codigo, p2.nombre, p2.precio_neto, "activo")
insertar_producto(p3.codigo, p3.nombre, p3.precio_neto, "activo")
lista_productos=[p1,p2,p3]




#--------------------registro del cliente----------------------------
print("hola bienvenido al sistema para registrarse y comprar en kioskofeliz,")
nombre = input("Nombre del cliente: ")
email = input("Email del cliente: ")
rut = input("rut del cliente: ")
nivel = input("Nivel del cliente (General / estudiante): ")
password = input("Por favor ingresa una contraseña para tu cuenta: ")

#insertamos el cliente en la base de datos
insertar_cliente(rut, nombre, email, password, nivel,obtener_fecha_api())
clienteobj=cliente_module.cliente(nombre,email,rut,nivel,password)



#--------------------creacion del carrito----------------------------
carritoobj=carrito_module.carrito(clienteobj)
insertar_carrito(clienteobj.id_cliente,obtener_fecha_api(),carritoobj.subtotal,carritoobj.descuento_aplicado,carritoobj.total)










#
def inicio():
    while True:
        try:
            print("enorabuena ahora ya estas registrado en el sistema")
            time.sleep(1)
            print("====================================================")
            print("menu del kiosko")
            time.sleep(0.5)
            print("1: comprar productos")
            time.sleep(0.5)
            print("2: imprimir tiket")
            time.sleep(0.5)
            print("3: salir del sistema")
            opcion=int(input("elige una opcion porfavor: "))
            if 1 <= opcion <= 3:
                if opcion==1:
                    while True:    
                        try:
                            for i in lista_productos:
                                print (i)
                                time.sleep(0.5)
                            print("elige un producto y una cantidad de esta lista porfavor")
                            time.sleep(0.5) 
                            prod=int(input("elige un producto estan enumerados del 1 al 10: "))
                            if 1 <= prod <= 10:
                                cantidad=int(input("porfavor indica una cantidad: "))
                                prod_elegido=lista_productos[prod-1]
                                carritoobj.agregar_items(prod_elegido,cantidad)                   
                                print(f"se agregaron {cantidad} de {prod_elegido.nombre}")
                                print("desea agregar otro producto? s/n")
                                otro_prod=input("").lower()
                                if otro_prod !="s":
                                    break 
                            else:   
                                print("Opción inválida")                            
                        except ValueError:
                                print("numero incorrecto y/o fuera de rango")   
                elif opcion==2:
                    carritoobj.ticket()
                    break
                elif opcion==3:
                    print("gracias por usar el sistema hasta pronto")
                    break                
        except ValueError:
            print("opcion no valida o caracter invalido porfavor ingresa un numero entre 1 y 3 :D")
        #lo pude hacer desde el if para que no se repitan las opciones la embarre jsjsjs    
        #nisiquiera quise poner lineas de comentarios dentro de esta estructura
        #me costo practicamente mi sanidad mental entera en que funcionara 
        #12:023 de la noche y aqui ando xnjakcan
        #al final estaba mal porque estaba desordenado el codigo nomas csm
        
inicio()


