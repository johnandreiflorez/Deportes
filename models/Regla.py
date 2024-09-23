import datetime;
class regla:
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
        
    fechaCreacion: datetime = "";
    def GetFechaCreacion(self) -> datetime:
        return self.fechaCreacion;
    def SetFechaCreacion(self, value: datetime) -> None:
        self.fechaCreacion = value;

    deporteId: int = 0;
    def GetDeporteId(self) -> int:
        return self.deporteId;
    def SetDeporteId(self, value: int) -> None:
        self.deporteId = value;
    
    
    
    