import socket

# Endereço e porta em que o servidor vai escutar
host = '127.0.0.1'
port = 12345

# Cria um objeto de socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincula o socket ao endereço e porta especificados
udp_socket.bind((host, port))

print(f"Servidor UDP aguardando conexões em {host}:{port}")

while True:
    # Recebe dados e endereço do cliente
    data, addr = udp_socket.recvfrom(1024)
    
    print(f"Recebido de {addr}: {data.decode('utf-8')}")

    # Aqui você pode adicionar lógica para processar os dados recebidos

# Feche o socket quando terminar
udp_socket.close()
