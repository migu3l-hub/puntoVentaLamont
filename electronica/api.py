import json
from django.contrib.auth.hashers import check_password, make_password
import socket



def validar_password(pwd_enviada, pwd_bd):
    return check_password(pwd_enviada, pwd_bd)


def hashear_contrasena(password):
    return make_password(password)

def servidor_activo(ip_srv,puerto):
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


