import socket

HOST = '127.0.0.1'
PORT = 176

s = socket.socket()
s.connect((HOST, PORT))

print('[-] Start Client')
print('[-] Wainting Serve...')
print(f'[-] Connect to the serve: {HOST}')

while True:
    data = s.recv(2048)
    command = data.decode('utf-8')
    if command == 'd-':
        print('Connect Off')
        exit()
    print(f'Serve say {command}')
