from db.config import Session
from db.factory.factory import crearEstados,crearCotizacion,crearClientes

session = Session()

def menu():
    while True:
        print("0) Salir\n"
              "1) Crear estados \n"
              "2) Crear Clientes\n"
              "3) Crear Cotizacion\n")

        opc = int(input("Dime que quieres hacer: "))
        if opc == 1:
            crearEstados()
        elif opc == 2:
            crearClientes()
        elif opc == 3:
            crearCotizacion()
        else:
            break


if __name__ == '__main__':
    menu()


