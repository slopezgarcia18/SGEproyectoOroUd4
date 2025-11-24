from services.services import (insertarCliente,getClienteByDni,getVentasMes,
                               getVentasCliente,getTasaNoAceptadas,getClienteMasVentas,getClienteMesesSinVenta)

# Aqui se insertan los metodos/funciones

class Gestor:
    def __init__(self, session):
        self.session = session

    def insertClient(self):
        insertarCliente()

    def getClientByDni(self,dni):
        getClienteByDni(dni)

    def getVentasMes(self,mes):
        getVentasMes(mes)

    def getVentasCliente(self,nombre):
        getVentasCliente(nombre)

    def getTasasNoAceptadas(self):
        getTasaNoAceptadas()

    def getClientesMasVentas(self):
        getClienteMasVentas()

    def getClientesNoVentasMes(self):
        getClienteMesesSinVenta()