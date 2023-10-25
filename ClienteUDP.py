import socket

# Endereço e porta do servidor UDP
server_host = '127.0.0.1'
server_port = 12345

# Cria um objeto de socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input("Digite uma mensagem para enviar ao servidor (ou 'exit' para sair): ")

    if mensagem.lower() == 'exit':
        break

    # Envia a mensagem para o servidor
    udp_socket.sendto(mensagem.encode('utf-8'), (server_host, server_port))

# Fecha o socket quando terminar
udp_socket.close()
