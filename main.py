from clases import clase_carrito as carrito_module
from clases import clase_cliente as cliente_module
from clases import clase_producto as producto_module

import time 
id_cliente_codigo=1
id_carrito_actual=1103

#si lo se se que no seria factible en practica pero al igual que en base de datos eso se arregla con un for y un args para que cada que inicie un 
# cliente se sume uno al contador
#lo mismo va para el carrito, eso creo que no es parte de la evaluacion asi que esta bien de todos modos :D

p1 = producto_module.producto(1, "Café", 2500)
p2 = producto_module.producto(2, "Pan", 1000)
p3 = producto_module.producto(3, "te", 500)
p4 = producto_module.producto(4, "dona", 2500)
p5 = producto_module.producto(5, "latte", 2000)
p6 = producto_module.producto(6, "pan_dulce", 1000)
p7 = producto_module.producto(7, "moka latte", 3000)
p8 = producto_module.producto(8, "pan japones", 5000)
p9 = producto_module.producto(9, "pastel de luna", 3500)
p10 = producto_module.producto(10, "cruassant", 1500)

lista_productos=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]



print("hola bienvenido al sistema para registrarse y comprar en kioskofeliz,")
nombre = input("Nombre del cliente: ")
email = input("Email del cliente: ")
rut = input("rut del cliente: ")
nivel = input("Nivel del cliente (General / estudiante): ")

clienteobj=cliente_module.cliente(nombre,email,rut,id_cliente_codigo,nivel)
carritoobj=carrito_module.carrito(id_carrito_actual,clienteobj)

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


