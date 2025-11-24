#Instanciar con faker

import random
from faker import Faker

from db.config import Session
from db.models.models import Estado, Cliente, Cotizacion, Venta

from datetime import date, timedelta
import datetime

fake = Faker('es_ES')

session = Session()

def crearEstados():

    listaEstados = ["TASACIÓN", "ACEPTADA", "RECHAZADA"]

    for nombre in listaEstados:
        #Filtro los nombres para comprobar si existe
        existe = session.query(Estado).filter_by(nombre = nombre).first()

        if not existe:
            nuevoEstado = Estado(nombre = nombre)
            session.add(nuevoEstado)
            print(f"El estado {nombre} ha sido añadido a la base de datos")
        else:
            print(f"El estado {nombre} ya existe")

    session.commit()
    print("Estados guardados correctamente")

def crearClientes():

    for i in range(18):
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
    print("Clientes guardados correctamente")

def crearCotizacion():
    # cada registro del precio debe tener en cuenta el precio del registro anterior
    precioOro = 113002

    fechaInicio = date(2025,1,1)
    fechaFin = date.today()
    fechaActual = fechaInicio

    while fechaActual <= fechaFin:
        bajadaOro = precioOro - (random.randint(1, 3) * precioOro / 100)
        subidaOro = precioOro + (random.randint(1, 3) * precioOro / 100)
        # Creo una lista para poder utilizar random.choice y elegir una de las dos opciones
        fluctuacion = [bajadaOro, subidaOro]
        valorOroActual = random.choice(fluctuacion)

        nuevaCoti = Cotizacion(
            fecha = fechaActual,
            precio = valorOroActual
        )

        session.add(nuevaCoti)
        precioOro = valorOroActual
        fechaActual += timedelta(days=1)

    session.commit()
    print("Los registros de cotizacion han sido creados correctamente")


def crearVentas():
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




















