import socket

host = '192.168.56.1'
port = 176

def comando(mensagem):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))
    print(f"Servidor UDP aguardando conexões em {host}:{port}")
    udp_socket.sendto(mensagem.encode('utf-8'), (host, port))
