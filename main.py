from db.config import Session
from db.factory.factory import crearEstados, crearCotizacion, crearClientes, crearVentas
from gestion.gestion import Gestor

session = Session()

def menu():
    gestor = Gestor(session)

    while True:
        print("0) Salir\n"
              "1) Alta Cliente \n"
              "2) Buscar cliente\n"
              "3) Ventas de un mes\n"
              "4) Ventas de cliente\n"
              "5) Tasaciones no aceptadas\n"
              "6) Clientes con mas ventas\n"
              "7) Clientes con 3 meses sin ventas")

        opc = int(input("Dime que quieres hacer: "))
        if opc == 1:
            gestor.insertClient()
        elif opc == 2:
            dniCliente = input("Inserte el dni: ")
            gestor.getClientByDni(dniCliente)
        elif opc == 3:
            mesVenta = int(input("Elige un mes del año: "))
            gestor.getVentasMes(mesVenta)
        elif opc == 4:
            nombreCliente = input("Nombre del cliente: ")
            gestor.getVentasCliente(nombreCliente)
        elif opc == 5:
            gestor.getTasasNoAceptadas()
        elif opc == 6:
            gestor.getClientesMasVentas()
        elif opc == 7:
            gestor.getClientesNoVentasMes()
        else:
            break

    print("Nos vemos!")

if __name__ == '__main__':
    menu()


