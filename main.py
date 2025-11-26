from db.config import session
from gestion.gestion import Gestor
from log.log import Log

gestor = Gestor(session)
logger = Log()

def menu():
    # Creo los estados por primera vez
    gestor.crearEstados()
    # Creo los clientes por primera vez
    gestor.crearClientes()
    # Creo los precios por primera vez
    gestor.crearCotizacion()
    # Creo las ventas por primera vez
    gestor.crearVentas()
    while True:
        print("0) Salir\n"
              "1) Alta Cliente\n"
              "2) Buscar cliente\n"
              "3) Ventas de un mes\n"
              "4) Ventas de cliente\n"
              "5) Tasaciones no aceptadas\n"
              "6) Clientes con mas ventas\n"
              "7) Clientes con 3 meses sin ventas\n"
              "8) Grafica oro\n"
              "9) Grafica ventas totales por mes\n"
              "10) Insertar nueva venta\n"
              "11) Cambiar estado de una venta\n"
              "12) Dar de baja a cliente")

        opc = int(input("Dime que quieres hacer: "))
        if opc == 1:
            logger.log("info","Alta cliente")
            gestor.insertClient()
        elif opc == 2:
            logger.log("info", "Buscar cliente")
            dniCliente = input("Inserte el dni: ")
            gestor.getClientByDni(dniCliente)
        elif opc == 3:
            logger.log("info", "Ventas realizadas en un mes")
            mesVenta = int(input("Elige un mes del año: "))
            gestor.getVentasMes(mesVenta)
        elif opc == 4:
            logger.log("info", "Ventas que ha realizado un cliente")
            idCliente = int(input("Id del cliente: "))
            gestor.getVentasCliente(idCliente)
        elif opc == 5:
            logger.log("info", "Tasaciones que no se encuentran aceptadas")
            gestor.getTasasNoAceptadas()
        elif opc == 6:
            logger.log("info", "Cliente que más ventas ha realizado")
            gestor.getClientesMasVentas()
        elif opc == 7:
            logger.log("info", "Clientes que no realizan una venta en un periodo de 3 meses")
            gestor.getClientesNoVentasMes()
        elif opc == 8:
            logger.log("info", "Grafica cantidad de oro vendido por cliente")
            gestor.graficaOro()
        elif opc == 9:
            logger.log("info", "Grafica total de ventas por mes")
            gestor.graficaVentasMes()
        elif opc == 10:
            logger.log("info", "Insertar nueva venta")
            gestor.crearVenta()
        elif opc == 11:
            gestor.cambiarEstado()
        elif opc == 12:
            idCliente = int(input("Id del cliente: "))
            gestor.bajaCliente(idCliente)
        else:
            break

    print("Saliendo del sistema...")

if __name__ == '__main__':
    menu()


