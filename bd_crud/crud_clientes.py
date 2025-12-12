import oracledb
from datetime import datetime
from .conexion_oracle import obtener_conexion
from clases.clase_cliente import cliente

# insertar un nuevo cliente en la tabla CLIENTE
def insertar_cliente(id_cliente: int, rut: str, nombre: str, email: str, contrasena: str, nivel: str, fecha_registro: str) -> None:  # type: ignore
    conexion = None
    cursor = None
    try:
        # Convert nivel string to NUMBER: "General" -> 1, "estudiante" -> 0
        nivel_num = 1 if nivel.lower() == "general" else 0
        
        # Parse fecha string - try multiple formats
        fecha_dt = None
        for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]:
            try:
                fecha_dt = datetime.strptime(fecha_registro, fmt)
                break
            except ValueError:
                continue
        
        if fecha_dt is None:
            print(f"Error: Formato de fecha no reconocido: {fecha_registro}")
            return
        
        conexion = obtener_conexion()
        if conexion is None:
            print("Error: No se pudo conectar a la base de datos")
            return
        
        cursor = conexion.cursor() # type: ignore

        cursor.execute(""" 
            INSERT INTO CLIENTE (
                ID_CLIENTE,
                RUT,
                NOMBRE,
                EMAIL,
                CONTRASENA_HASH,
                NIVEL,
                FECHA_REGISTRO
            ) VALUES (
                :id_cliente,
                :rut,
                :nombre,
                :email,
                :contrasena,
                :nivel,
                :fecha_registro
            )
        """, {
            "id_cliente": id_cliente,
            "rut": rut,
            "nombre": nombre,
            "email": email,
            "contrasena": contrasena,
            "nivel": nivel_num,
            "fecha_registro": fecha_dt
        })

        conexion.commit()
        print("Cliente insertado correctamente")

    except oracledb.DatabaseError as e:
        print(f"Error al insertar cliente: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
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
    # Basic smoke test: print existing clients (avoid inserting when running module directly)
    seleccionar_clientes()