import socket

HOST = '127.0.0.1'
PORT = 176

s = socket.socket()
s.bind((HOST, PORT))

print('[+] Start Serve')
print('[+] Wainting Connection')
s.listen(1)
client, client_addr = s.accept()
print(f'[+] {client_addr} Connect to the serve')

while True:
    command = input('Enter Command:')
    client.send(bytes(str(command), 'utf-8'))
    if command == 'd-':
        print('End Connection')
        exit()
    print('[+] Command Send')
    #output = client.recv(1024)
    #output = client.decode(encoding='utf-8')
    #print(f'Output: {output}')
