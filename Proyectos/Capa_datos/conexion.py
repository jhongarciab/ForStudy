from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'Test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Xevaxtiam1'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                print(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                print(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        print(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        print(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
   conexion1 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion1)
   conexion2 = Conexion.obtenerConexion()
   conexion3 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion3)
   conexion4 = Conexion.obtenerConexion()
   conexion5 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion5)
   conexion6 = Conexion.obtenerConexion()