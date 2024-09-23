from controllers.DeporteController import DeporteController;
from models.Deporte import deporte   

if __name__ == "__main__":
     # Crear una instancia del controlador
    controlador = DeporteController()
    
    # Definir los datos del deporte que se van a insertar
    newDeporte = deporte()
    newDeporte.SetNombre("oscar")
    newDeporte.SetDescripcion("cardenass")
    
    # Llamar al método que inserta un deporte
    controlador.Create(newDeporte)
    # Llamar al método para obtener los deportes desde la base de datos
    respuesta = controlador.GetAll()
    # Mostrar los deportes obtenidos
    controlador.ShowItems(respuesta)

    
    
    