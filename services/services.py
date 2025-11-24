#Realizar aquí las consultas
from calendar import month
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

from sqlalchemy import extract
from sqlalchemy.sql.functions import count

from db.factory.factory import session
from db.models.models import Cliente, Venta, Estado


def insertarCliente():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nac = input("Fecha nacimiento (AAAA/MM/DD): ")
    dni = input("Dni: ")
    email = input("Email: ")
    nacionalidad = input("Nacionalidad: ")
    telefono = int(input("Telefono: "))
    direccion = input("Dirección: ")

    nuevoCliente = Cliente(
        nombre=nombre,
        apellidos=apellidos,
        fecha_nacim=datetime.strptime(fecha_nac, "%Y/%m/%d").date(),
        dni=dni,
        email=email,
        nacionalidad=nacionalidad,
        telefono=telefono,
        direccion=direccion
    )
    session.add(nuevoCliente)

    session.commit()
    print("Cliente guardado correctamente")

def getClienteByDni(dniCliente):
    clienteDNI = session.query(Cliente).all()
    existe = False

    for cliente in clienteDNI:
        if cliente.dni == dniCliente:
            print(cliente)
            existe = True

    if not existe:
        print("El cliente no existe en la base de datos. Compruebe si ha insertado correctamente el dni")

def getVentasMes(mesVenta):
    ventas = session.query(Venta).filter(extract("month", Venta.fecha_venta) == mesVenta).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        print(f"No hay ventas en el mes {mesVenta}")

def getVentasCliente(nombre):
    # Añado [0] al final para que solo me devuelva el primer valor de la TUPLA (Ejem: si sale [1,], con [0] cojo el 1)
    cliente = session.query(Cliente.id).filter(Cliente.nombre == nombre).first()[0]
    ventas = session.query(Venta).filter(Venta.id_cliente == cliente).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        print(f"El cliente no ha realizado ninguna venta")

def getTasaNoAceptadas():
    estado = [r[0] for r in session.query(Estado.id).filter(Estado.nombre.in_(["RECHAZADA","TASACIÓN"])).all()]
    ventas = session.query(Venta).filter(Venta.id_estado.in_(estado)).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        print("No se han encontrado las ventas")

def getClienteMasVentas():
    ventas = session.query(Venta.id_cliente).group_by(Venta.id_cliente).order_by(count(Venta.id_cliente).desc()).first()[0]

    cliente = session.query(Cliente).filter(Cliente.id == ventas).first()

    if cliente:
        print(cliente)
    else:
        print("No existe el cliente")

def getClienteMesesSinVenta():
    tresMesesAtras = date.today() - relativedelta(months=3)

    cliente = (session.query(Cliente)
               .join(Venta, Venta.id_cliente == Cliente.id)
               .filter(Venta.fecha_venta < tresMesesAtras).all())

    if cliente:
        for cli in cliente:
            print(cli)
    else:
        print("No existe datos de clientes")








