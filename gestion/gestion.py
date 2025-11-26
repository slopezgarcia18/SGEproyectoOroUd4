
from services.services import (insertarCliente, getClienteByDni, getVentasMes,
                               getVentasCliente, getTasaNoAceptadas, getClienteMasVentas,
                               getClienteMesesSinVenta, graficaOro, graficaVentasMes,
                               cambiarVentaEstado, insertarVenta, bajaCliente)

from db.factory.factory import *

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

    def graficaOro(self):
        graficaOro()

    def graficaVentasMes(self):
        graficaVentasMes()

    def cambiarEstado(self):
        cambiarVentaEstado()

    def crearVenta(self):
        insertarVenta()

    def crearClientes(self):
        crearClientes()

    def crearVentas(self):
        crearVentas()

    def crearEstados(self):
        crearEstados()

    def crearCotizacion(self):
        crearCotizacion()

    def bajaCliente(self,idCliente):
        bajaCliente(idCliente)