import oracledb
from conexion_oracle import obtener_conexion
from clases.clase_cliente import cliente
#el cursor es el que permite ejecutar las consultas SQL en la base de datos
#insertar un nuevo cliente en la tabla CLIENTE
def insertar_cliente(rut, nombre, email, contrasena, nivel,fecha_registro): # type: ignore
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor() # type: ignore

        cursor.execute(""" 
            INSERT INTO CLIENTE (
                ID_CLIENTE,
                RUT,
                NOMBRE,
                EMAIL,
                CONTRASENA_HASH,
                NIVEL
                fecha_registro
            ) VALUES (
                :id_cliente,
                :rut,
                :nombre,
                :email,
                :contrasena,
                :nivel
                :fecha_registro
            )
        """, {
            "id_cliente": cliente.id_cliente,
            "rut": rut,
            "nombre": nombre,
            "email": email,
            "contrasena": contrasena,
            "nivel": nivel,
            "fecha_registro": fecha_registro
        })

        conexion.commit()
        print("Cliente insertado correctamente")

    except oracledb.DatabaseError as e:
        print(f"Error al insertar cliente: {e}")

    finally:
        cursor.close()
        conexion.close()





#seleccionar todos los clientes de la tabla CLIENTE
def seleccionar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM CLIENTE")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)

    except oracledb.DatabaseError as e:
        print(f"Error en la consulta: {e}")
        return []

    finally:
        cursor.close()
        conexion.close()






#update del email de un cliente en la tabla CLIENTE
def actualizar_email_cliente(id_cliente, nuevo_email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE CLIENTE
            SET EMAIL = :nuevo_email
            WHERE ID_CLIENTE = :id_cliente
        """, {
            "nuevo_email": nuevo_email,
            "id_cliente": id_cliente
        })
        conexion.commit()
        print("Email del cliente actualizado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al actualizar el email del cliente: {e}")

    finally:
        cursor.close()
        conexion.close()



#delete de un cliente en la tabla CLIENTE
def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            DELETE FROM CLIENTE
            WHERE ID_CLIENTE = :id_cliente
        """, {
            "id_cliente": id_cliente
        })
        conexion.commit()
        print("Cliente eliminado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar el cliente: {e}")

    finally:
        cursor.close()
        conexion.close()

#pruebas
if __name__ == "__main__":
    insertar_cliente(2, "98765432-1", "Juan Perez", "EMAIL@EXAMPLE.COM", 1, 1,"2024-06-01")
    seleccionar_clientes()
    actualizar_email_cliente(2, "nuevo_email@example.com")
    eliminar_cliente(2)