import time
import struct
import scapy.all as scapy
import random
import string
import os
from cesar import texto_cifrado

# Obtener el número de proceso del sistema para usar como id (si se desea usar PID)
id_ipv4 = os.getpid() & 0xFFFF  # Aseguramos que el ID esté en el rango de 16 bits
id_icmp = id_ipv4  # Usar el mismo identificador para todos los paquetes

# Obtener el timestamp actual en milisegundos
timestamp = struct.pack("<Q", int(time.time()))

# Ingresar IP de destino y mensaje cifrado
ip_dst = input("IP de destino: ")

# Crear y enviar paquetes ICMP request con el mensaje cifrado
packets = []
for i, caracter in enumerate(texto_cifrado.strip('"')):
    # Relleno aleatorio inicial (39 bytes) más 8 bytes adicionales
    relleno_aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=47))
    payload = timestamp + relleno_aleatorio.encode() + caracter.encode()
    
    # Crear el paquete ICMP
    packet = scapy.IP(dst=ip_dst, id=id_ipv4, flags="DF") / scapy.ICMP(id=id_icmp, seq=i + 1) / payload
    packets.append(packet)

# Enviar los paquetes generados
scapy.send(packets)