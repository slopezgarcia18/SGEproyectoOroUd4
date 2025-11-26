#Realizar aquí las consultas
import re
from datetime import date
from dateutil.relativedelta import relativedelta

from sqlalchemy import extract
from sqlalchemy.sql.functions import count, func

from db.factory.factory import session
from db.models.models import Cliente, Venta, Estado, Cotizacion

import matplotlib.pyplot as plt

from log.log import  *


logger = Log()


def insertarCliente():
    clienteExistente = int(input("Dar de alta a cliente existente(1)\n"
                                 "Dar de alta a un nuevo cliente(2)"))
    if clienteExistente == 1:
        idCliente = int(input("Inserte el id del cliente: "))
        clienteID = session.query(Cliente).filter(Cliente.id == idCliente).first()

        if clienteID:
            clienteID.activo = True
            session.commit()
            logger.log("info",f"El cliente con id {idCliente} ha sido dado de alta de nuevo en la BD")
        else:
            logger.log("error",f"El cliente con id {idCliente} no existe")
    elif clienteExistente == 2:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha_nac = input("Fecha nacimiento (AAAA/MM/DD): ")
        dni = input("Dni: ")
        email = input("Email: ")
        nacionalidad = input("Nacionalidad: ")
        telefono = input("Telefono: ")
        direccion = input("Dirección: ")

        fecha = datetime.strptime(fecha_nac,"%Y/%m/%d").date()
        difDias = (date.today() - fecha)
        edad = int(difDias.days / 365.25)
        expRegularEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        try:
            # Validacion de campos vacios
            if not nombre or not nombre.strip():
                logger.log("error", "El campo nombre no puede estar vacío")
                return
            if not apellidos or not apellidos.strip():
                logger.log("error", "El campo apellidos no puede estar vacío")
                return
            if not fecha_nac or not fecha_nac.strip():
                logger.log("error", "El campo fecha Nacimiento no puede estar vacío")
                return
            if not dni or not dni.strip():
                logger.log("error", "El campo dni no puede estar vacío")
                return
            if not email or not email.strip():
                logger.log("error", "El campo email no puede estar vacío")
                return
            if not nacionalidad or not nacionalidad.strip():
                logger.log("error", "El campo nacionalidad no puede estar vacío")
                return
            if not direccion or not direccion.strip():
                logger.log("error", "El campo direccion no puede estar vacío")
                return

            # Validacion email
            if not re.fullmatch(expRegularEmail, email):
                logger.log("error","El campo email debe tener un formato correcto (ejemplo@ejemplo.com/es)")
                return

            # Validacion de edad
            if edad < 18:
                logger.log("error", "El usuario debe ser mayor de edad")
                return

            # Validacion de numero telefono
            telefCliente = int(telefono)
        except:
            logger.log("error", "Compruebe los datos introducidos")
            return

        nuevoCliente = Cliente(
            nombre=nombre,
            apellidos=apellidos,
            fecha_nacim=datetime.strptime(fecha_nac, "%Y/%m/%d").date(), #Siempre será mayor de edad porque está puesto en el model
            dni=dni,
            email=email,
            nacionalidad=nacionalidad,
            telefono=telefCliente,
            direccion=direccion
        )
        session.add(nuevoCliente)

        session.commit()
        logger.log("info","Cliente guardado correctamente")
    else:
        logger.log("error","Inserte un número valido (1/2)")

def bajaCliente(idCliente):
    cliente = session.query(Cliente).filter(Cliente.id == idCliente).first()

    if cliente:
        cliente.activo = False
        session.commit()
        logger.log("info",f"El cliente con id {idCliente} ha sido dado de baja")
    else:
        logger.log("error",f"No existe un cliente con id {idCliente}")

def getClienteByDni(dniCliente):
    clienteDNI = session.query(Cliente).filter(Cliente.dni == dniCliente).first()

    if clienteDNI:
        print(clienteDNI)
    else:
        logger.log("error", "El cliente no existe en la base de datos. Compruebe si ha insertado correctamente el dni")


def getVentasMes(mesVenta):
    ventas = session.query(Venta).filter(extract("month", Venta.fecha_venta) == mesVenta).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        logger.log("error",f"No hay ventas en el mes {mesVenta}")

def getVentasCliente(id):
    # Añado [0] al final para que solo me devuelva el primer valor de la TUPLA (Ejem: si sale [1,], con [0] cojo el 1)
    cliente = session.query(Cliente.id).filter(Cliente.id == id).first()[0]
    ventas = session.query(Venta).filter(Venta.id_cliente == cliente).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        logger.log("error",f"El cliente no ha realizado ninguna venta")

def getTasaNoAceptadas():
    estado = [r[0] for r in session.query(Estado.id).filter(Estado.nombre.in_(["RECHAZADA","TASACIÓN"])).all()]
    ventas = session.query(Venta).filter(Venta.id_estado.in_(estado)).all()

    if ventas:
        for ven in ventas:
            print(ven)
    else:
        logger.log("error","No se han encontrado las ventas")

def getClienteMasVentas():
    ventas = session.query(Venta.id_cliente).group_by(Venta.id_cliente).order_by(count(Venta.id_cliente).desc()).first()[0]

    cliente = session.query(Cliente).filter(Cliente.id == ventas).first()

    if cliente:
        print(cliente)
    else:
        logger.log("error","No existe el cliente")

def getClienteMesesSinVenta():
    tresMesesAtras = date.today() - relativedelta(months=3)

    cliente = (session.query(Cliente)
               .join(Venta, Venta.id_cliente == Cliente.id)
               .filter(Venta.fecha_venta < tresMesesAtras).all())

    if cliente:
        for cli in cliente:
            print(cli)
    else:
        logger.log("error","No existe datos de clientes")

def graficaOro():
    # Select del nombre del cliente y la suma de sus cantidades de ventas, agrupado por nombre
    ventasCliente = (session.query(Cliente.nombre,func.sum(Venta.cantidad))
                     .join(Cliente, Cliente.id == Venta.id_cliente)
                     .group_by(Cliente.nombre).all())

    # Creo dos listas para representar la grafica
    listaNombres = []
    listaCantidad = []

    #bucle con la dos columnas de la consulta
    for nombre,cantidad in ventasCliente:
        listaNombres.append(nombre)
        listaCantidad.append(cantidad)

    plt.bar(listaNombres,listaCantidad)
    plt.title("Cantidad de oro total por cliente")
    plt.xlabel("Nombre")
    plt.ylabel("Cantidad")
    plt.show()

def graficaVentasMes():
    ventasMes = (session.query(func.extract('month',Venta.fecha_venta), func.count(Venta.id))
                 .group_by(extract('month',Venta.fecha_venta)).all())

    listaMeses = []
    listaVentas = []

    for mes,totalVentas in ventasMes:
        listaMeses.append(mes)
        listaVentas.append(totalVentas)

    plt.bar(listaMeses, listaVentas)
    plt.title("Total ventas por mes")
    plt.xlabel("Meses")
    plt.ylabel("Total Ventas")
    plt.show()

def cambiarVentaEstado():
    ventaID = int(input("Inserte el id de la venta: "))

    try:
        idVenta = int(ventaID)
    except:
        logger.log("error","Introduce un número entero")
        return

    venta = session.query(Venta).filter(Venta.id == idVenta).first()

    if venta:
        estadoNombre = input("A que estado quieres cambiar ('ACEPTADA' o 'RECHAZADA'): ")
        estados = session.query(Estado.id).filter(func.upper(Estado.nombre) == estadoNombre.upper()).first()[0]

        if venta.id_estado == estados:
            logger.log("warning","Ya tiene ese estado")
        elif not estados:
            logger.log("error","No existe ese estado")
        else:
            cotizacion = session.query(Cotizacion).filter(Cotizacion.fecha == date.today()).first()
            venta.id_estado = estados
            if cotizacion:
                venta.fecha_venta = cotizacion.fecha
                venta.id_precio = cotizacion.id

                session.commit()
                logger.log("info",f"El estado ha sido modificado a {estadoNombre}")
    else:
        logger.log("error","No existe cotizacion")


def insertarVenta():
    id = input("Inserte el id del cliente: ")
    estadoTasacion = "TASACIÓN"
    oro = input("Introduce la cantidad de oro en gramos para la tasación")

    try:
        idcliente = int(id)
        cantidadOro = int(oro)
    except:
        logger.log("error","Introduce un número válido")
        return

    cliente = session.query(Cliente.id).filter(Cliente.id == idcliente).filter(Cliente.activo == True).first()
    estado = session.query(Estado.id).filter(func.upper(Estado.nombre) == estadoTasacion.upper()).first()[0]
    cotizacion = session.query(Cotizacion).filter(Cotizacion.fecha == date.today()).first()

    if cliente:
        nuevaVenta = Venta(
            fecha_venta = date.today(),
            id_cliente = idcliente,
            id_precio = cotizacion.id,
            id_estado = estado,
            cantidad = cantidadOro
        )
        session.add(nuevaVenta)
        session.commit()
        logger.log("info","Venta realizada exitosamente!")
    else:
        logger.log("error","No existe el cliente o está dado de baja")












