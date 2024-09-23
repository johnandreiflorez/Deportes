from models.Regla  import regla
class deporte:
    id: int = 0;
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    nombre: str = "";
    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;
        
    descripcion: str = "";
    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value;   
    reglas = []
    def AddRegla(self, currentRegla: regla):
        self.reglas.append(currentRegla)
