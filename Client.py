import socket

HOST = "192.168.0.111"  # The server's hostname or IP address
PORT = 176  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while True:

        s.connect((HOST, PORT))
        connect = s.recv(1024)
        tests = connect.decode('utf-8')
        confirm = 'Conectado'
        if confirm == tests:
            while True:
                command = input("Connect>>>")
                s.sendall(bytes(str(command), 'utf-8'))
                try:
                    data = s.recv(2048)
                    saidapc = data.decode("utf-8")
                    print(f"Received {saidapc}")
                except:
                    print(f"invalid command:{command}")
                    pass
                if command == 'd-':
                    print('Connect Off')
                    break
