from controllers.conexion import Conexion
from models.Deporte import deporte
from models.Regla import regla

class DeporteController:
    def __init__(self):
        self.conexion = Conexion()

    def GetAll(self):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion FROM deporte"
        resultados = self.conexion.ejecutar_query(consulta)
        deportes = []
        for fila in resultados:
            curretnDeporte = deporte()
            curretnDeporte.SetId(fila[0])
            curretnDeporte.SetNombre(fila[1])
            curretnDeporte.SetDescripcion(fila[2])
            deportes.append(curretnDeporte)
        self.conexion.cerrar()
        return deportes

    def GetById(self, id):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion FROM deporte WHERE id = ?"
        resultado = self.conexion.ejecutar_query(consulta, [id])
        if resultado:
            fila = resultado[0]
            curretnDeporte = deporte()
            curretnDeporte.SetId(fila[0])
            curretnDeporte.SetNombre(fila[1])
            curretnDeporte.SetDescripcion(fila[2])
            self.conexion.cerrar()
            return curretnDeporte
        self.conexion.cerrar()
        return None

    def GetByName(self, nombre):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion FROM deporte WHERE nombre = ?"
        resultado = self.conexion.ejecutar_query(consulta, [nombre])
        deportes = []
        for fila in resultado:
            curretnDeporte = deporte()
            curretnDeporte.SetId(fila[0])
            curretnDeporte.SetNombre(fila[1])
            curretnDeporte.SetDescripcion(fila[2])
            deportes.append(curretnDeporte)
        self.conexion.cerrar()
        return deportes

    def Create(self, deporte: deporte):
        self.conexion.conectar()
        consulta = "INSERT INTO deporte (nombre, descripcion) VALUES (?, ?)"
        self.conexion.ejecutar_query((consulta, [deporte.GetNombre(), deporte.GetDescripcion()]))
        self.conexion.cerrar()

    def Update(self, deporte: deporte):
        self.conexion.conectar()
        consulta = "UPDATE deporte SET nombre = ?, descripcion = ? WHERE id = ?"
        self.conexion.ejecutar_query(consulta, [deporte.GetNombre(), deporte.GetDescripcion(), deporte.GetId()])
        self.conexion.cerrar()

    def Delete(self, id):
        self.conexion.conectar()
        consulta = "DELETE FROM deporte WHERE id = ?"
        self.conexion.ejecutar_query(consulta, [id])
        self.conexion.cerrar()

    def ShowItem(self, deporte: deporte):
        print(f"ID: {deporte.GetId()}, Nombre: {deporte.GetNombre()}, Descripción: {deporte.GetDescripcion()}")

    def ShowItems(self, deportes):
        for deporte in deportes:
            self.ShowItem(deporte)

    def GetAllRulesByDeportes(self):
        self.conexion.conectar();
        nameSp = "getRulesByDeporte"
        resultado = self.conexion.CallSP(nameSp);
        curretnDeporte = deporte()
        deportes = []
        sw = False
        for fila in resultado:
            if(curretnDeporte.GetId() != fila[0]):
                if(sw == True):
                    deportes.append(curretnDeporte)
                curretnDeporte = deporte()
                sw = True
            curretnDeporte.SetId(fila[0])
            curretnDeporte.SetNombre(fila[1])
            curretnDeporte.SetDescripcion(fila[2])
            curretnRegla = regla()
            curretnRegla.SetNombre(fila[3])
            curretnRegla.SetDescripcion(fila[4])
            curretnRegla.SetFechaCreacion(fila[5])
            curretnDeporte.AddRegla(curretnRegla)
        self.conexion.cerrar()
        return deportes