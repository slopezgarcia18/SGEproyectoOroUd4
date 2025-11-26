#Instanciar con faker

import random
from faker import Faker

from db.config import session
from db.models.models import Estado, Cliente, Cotizacion, Venta

from datetime import date, timedelta
from log.log import  *

fake = Faker('es_ES')


logger = Log()

def crearEstados():
    listaEstados = ["TASACIÓN", "ACEPTADA", "RECHAZADA"]

    for nombre in listaEstados:
        #Filtro los nombres para comprobar si existe
        existe = session.query(Estado).filter_by(nombre = nombre).first()

        if not existe:
            nuevoEstado = Estado(nombre = nombre)
            session.add(nuevoEstado)
            logger.log("info",f"El estado {nombre} ha sido añadido a la base de datos")

    session.commit()
    logger.log("info","Estados guardados correctamente")

def crearClientes():
    # Comprobar si ya existen datos
    countClientes = session.query(Cliente).count()
    if countClientes > 0:
        logger.log("info", "Los clientes ya existen en la base de datos. Omitiendo creación.")
        return

    for i in range(20):
        nuevoCliente = Cliente(
        nombre = fake.first_name(),
        apellidos = fake.last_name(),
        fecha_nacim = fake.date_of_birth(minimum_age=18),
        dni = fake.nif(),
        email = fake.email(),
        nacionalidad = fake.country(),
        telefono = fake.numerify('6########'),
        direccion = fake.street_address()
        )
        session.add(nuevoCliente)

    session.commit()
    logger.log("info","Clientes guardados correctamente")

def crearCotizacion():
    # cada registro del precio debe tener en cuenta el precio del registro anterior
    precioOro = 113002

    fechaInicio = date(2025,1,1)
    fechaFin = date.today()

    comprobarRegistro = session.query(Cotizacion.fecha).order_by(Cotizacion.fecha.desc()).first()

    if not comprobarRegistro:
        fecha = fechaInicio
    else:
        fecha = comprobarRegistro[0] + timedelta(days=1)

    while fecha <= fechaFin:
        bajadaOro = precioOro - (random.randint(1, 3) * precioOro / 100)
        subidaOro = precioOro + (random.randint(1, 3) * precioOro / 100)
        # Creo una lista para poder utilizar random.choice y elegir una de las dos opciones
        fluctuacion = [bajadaOro, subidaOro]
        valorOroActual = random.choice(fluctuacion)

        nuevaCoti = Cotizacion(
            fecha = fecha,
            precio = valorOroActual
        )

        session.add(nuevaCoti)
        precioOro = valorOroActual
        fecha += timedelta(days=1)

    session.commit()
    logger.log("info","Los registros de cotizacion han sido creados correctamente")


def crearVentas():
    # Comprobar si ya existen datos
    countVentas = session.query(Venta).count()
    if countVentas > 0:
        logger.log("info", "Las ventas ya existen en la base de datos. Omitiendo creación.")
        return

    estadoAceptada = session.query(Estado).filter(Estado.nombre == "ACEPTADA").first()
    estadoRechazada = session.query(Estado).filter(Estado.nombre == "RECHAZADA").first()
    estadoTasacion = session.query(Estado).filter(Estado.nombre == "TASACIÓN").first()

    cotizacion = session.query(Cotizacion).all()
    cliente = session.query(Cliente).all()

    for i in range(400):
        cotiRandom = random.choice(cotizacion)
        clienteRandom = random.choice(cliente)
        nuevaVenta = Venta(
            fecha_venta = cotiRandom.fecha,
            id_cliente = clienteRandom.id,
            id_precio = cotiRandom.id,
            id_estado = estadoAceptada.id,
            cantidad = random.randint(1,100)
        )
        session.add(nuevaVenta)

    for i in range(30):
        cotiRandom = random.choice(cotizacion)
        clienteRandom = random.choice(cliente)
        nuevaVenta = Venta(
            fecha_venta = cotiRandom.fecha,
            id_cliente = clienteRandom.id,
            id_precio = cotiRandom.id,
            id_estado = estadoRechazada.id,
            cantidad = random.randint(1,100)
        )
        session.add(nuevaVenta)

    for i in range(20):
        cotiRandom = random.choice(cotizacion)
        clienteRandom = random.choice(cliente)
        nuevaVenta = Venta(
            fecha_venta = cotiRandom.fecha,
            id_cliente = clienteRandom.id,
            id_precio = cotiRandom.id,
            id_estado = estadoTasacion.id,
            cantidad = random.randint(1,100)
        )
        session.add(nuevaVenta)

    session.commit()

























