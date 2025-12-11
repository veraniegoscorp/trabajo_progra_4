import oracledb
from conexion_oracle import obtener_conexion
def insertar_carrito(id, id_cliente, fecha_creacion, subtotal, descuento_aplicado, total): # type: ignore
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor() # type: ignore

        cursor.execute(""" 
            INSERT INTO CARRITO (
                ID_CARRITO,
                ID_CLIENTE,
                FECHA_CREACION,
                SUBTOTAL,
                DESCUENTO_APLICADO,
                TOTAL
            ) VALUES (
                :id_carrito,
                :id_cliente,
                :fecha_creacion,
                :subtotal,
                :descuento_aplicado,
                :total
            )
        """, {
            "id_carrito": id_carrito,
            "id_cliente": id_cliente,
            "fecha_creacion": fecha_creacion,
            "subtotal": subtotal,
            "descuento_aplicado": descuento_aplicado,
            "total": total
        })

        conexion.commit()
        print("Carrito insertado correctamente")

    except oracledb.DatabaseError as e:
        print(f"Error al insertar carrito: {e}")

    finally:
        cursor.close()
        conexion.close()