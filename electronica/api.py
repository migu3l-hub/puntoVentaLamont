import json
from django.contrib.auth.hashers import check_password, make_password
import socket


def validar_password(pwd_enviada, pwd_bd):
    return check_password(pwd_enviada, pwd_bd)


def hashear_contrasena(password):
    return make_password(password)


def servidor_activo(ip_srv, puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_srv, int(puerto)))
    if result == 0:
        return True
    else:
        return False


class ConeccionSrvMonitor(Exception):
    pass


def obtener_cpu(datos_servidor):
    dic = json.loads(datos_servidor)
    return float(dic.get('cpu'))


def obtener_memoria(datos_servidor):
    dic = json.loads(datos_servidor)
    return float(dic.get('memoria'))


def obtener_disco(datos_servidor):
    dic = json.loads(datos_servidor)
    return float(dic.get('disco'))


class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        cliente = self.session.get("cliente")
        if not carro:
            carro = self.session["carro"] = {}
        if not cliente:
            cliente = self.session["cliente"] = {}
        # else:
        self.carro = carro
        self.cliente = cliente

    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio_venta),
                "cantidad": 1,
                "stock": producto.stock
            }
        else:
            for key, value in self.carro.items():  # recorre la llave y el valor de la llave en el diccionario
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio_venta
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.precio_compra
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

    def agregar_cliente(self, cliente):

        self.eliminar_cliente()

        self.cliente[cliente.id] = {
            "cliente_id": cliente.id,
            "nombre": cliente.nombre,
            "apellidos": str(cliente.apellidos),
            "telefono": cliente.telefono
        }

        self.guardar_cliente()

    def guardar_cliente(self):
        self.session["cliente"] = self.cliente
        self.session.modified = True

    def eliminar_cliente(self):
        self.session["cliente"] = {}
        self.session.modified = True
