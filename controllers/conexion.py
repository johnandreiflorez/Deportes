from sqlite3 import Row
import pyodbc;

class Conexion:
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=deportes;
        PORT=3306;
        user=itm;
        password=Qwer.1234""";
    
    parametros_salidas: str='';
    
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = pyodbc.connect(self.string_conexion)
            self.cursor = self.conexion.cursor();
            print("Conexión exitosa a la base de datos.")
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")        
    
    def CallSP(self, nombreSP) :
        consulta: str = f"CALL {nombreSP}();";
        self.cursor.execute(consulta);
        return self.cursor;
            
    def ProcedimientoConSalida(self, nombreSP, parametrosInt, parametrosOut) -> Row:
        # conexion = pyodbc.connect(self.string_conexion);
        self.cursor = self.conexion.cursor();

        consulta = f"CALL {nombreSP}({self.generar_parametros(parametrosInt, parametrosOut)})"
        print(consulta)
        consulta2: str = f"SELECT {self.parametros_salidas};";
        print(consulta2)
        self.cursor.execute(consulta);


        self.cursor.execute(consulta2);
        
        resultado = self.cursor.fetchone()[0]

        return resultado;

    def generar_parametros(self, valores, salidas):
        # Convertir el primer arreglo (valores) en una cadena adecuada para SQL
        parametros_valores = [
            f"'{v}'" if isinstance(v, str) else str(v) for v in valores
        ]

        # Agregar las variables de salida con el formato @salida
        parametrossalidas = [f"@{s}" for s in salidas]
        self.parametros_salidas = ', '.join(parametrossalidas)
        # Combinar ambos arreglos en uno solo
        parametros_combinados = parametros_valores + parametrossalidas

        # Unir todo en una cadena separada por comas
        resultado = ', '.join(parametros_combinados)

        return resultado

    def obtener_resultado(self, consulta):
        """Ejecuta una consulta que devuelve un solo resultado."""
        try:
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchone()
            return resultado
        except pyodbc.Error as e:
            print(f"Error al obtener resultado: {e}")
            return None
    def ejecutar_query(self, consulta):
        """Ejecuta una consulta SQL."""
        try:
            self.cursor.execute(consulta)
            self.conexion.commit()
            print("Consulta ejecutada exitosamente.")
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")