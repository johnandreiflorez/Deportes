from controllers.conexion import Conexion
from models.Regla import regla

class ReglaController:
    def __init__(self):
        self.conexion = Conexion()

    def GetAll(self):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion, DeporteId, FechaCreacion FROM reglas"
        resultados = self.conexion.ejecutar_query(consulta)
        reglas = []
        for fila in resultados:
            curretnregla = regla()
            curretnregla.SetId(fila[0])
            curretnregla.SetNombre(fila[1])
            curretnregla.SetDescripcion(fila[2])
            curretnregla.SetDeporteId(fila[3])
            curretnregla.SetFechaCreacion(fila[4])
            reglas.append(curretnregla)
        self.conexion.cerrar()
        return reglas

    def GetById(self, id):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion, DeporteId, FechaCreacion FROM reglas WHERE id = ?"
        resultado = self.conexion.ejecutar_query(consulta, [id])
        if resultado:
            fila = resultado[0]
            curretnregla = regla()
            curretnregla.SetId(fila[0])
            curretnregla.SetNombre(fila[1])
            curretnregla.SetDescripcion(fila[2])
            curretnregla.SetDeporteId(fila[3])
            curretnregla.SetFechaCreacion(fila[4])
            self.conexion.cerrar()
            return curretnregla
        self.conexion.cerrar()
        return None

    def GetByName(self, nombre):
        self.conexion.conectar()
        consulta = "SELECT id, nombre, descripcion, DeporteId, FechaCreacion FROM reglas WHERE nombre = ?"
        resultado = self.conexion.obtener_resultado(consulta, [nombre])
        reglas = []
        for fila in resultado:
            curretnregla = regla()
            curretnregla.SetId(fila[0])
            curretnregla.SetNombre(fila[1])
            curretnregla.SetDescripcion(fila[2])
            curretnregla.SetDeporteId(fila[3])
            curretnregla.SetFechaCreacion(fila[4])
            reglas.append(curretnregla)
        self.conexion.cerrar()
        return reglas

    def Create(self, regla: regla):
        self.conexion.conectar()
        consulta = "INSERT INTO reglas (nombre, descripcion, deporteId) VALUES (?, ?, ?)"
        self.conexion.ejecutar_query(consulta, [regla.GetNombre(), regla.GetDescripcion(), regla.GetDeporteId])
        self.conexion.cerrar()

    def Update(self, regla: regla):
        self.conexion.conectar()
        consulta = "UPDATE regla SET nombre = ?, descripcion = ? WHERE id = ?"
        self.conexion.ejecutar_query(consulta, [regla.GetNombre(), regla.GetDescripcion(), regla.GetId()])
        self.conexion.cerrar()

    def Delete(self, id):
        self.conexion.conectar()
        consulta = "DELETE FROM regla WHERE id = ?"
        self.conexion.ejecutar_query(consulta, [id])
        self.conexion.cerrar()

    def ShowItem(self, regla: regla):
        print(f"ID: {regla.GetId()}, Nombre: {regla.GetNombre()}, Descripción: {regla.GetDescripcion()}")

    def ShowItems(self, reglas):
        for regla in reglas:
            self.ShowItem(regla)
    
    def AddRuleToSport(self, currtnregla: regla, nameSport: str):
        self.conexion.conectar();
