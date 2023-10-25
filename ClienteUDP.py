import socket
import os
from time import sleep
try:
    import pyautogui
    import keyboard
    from selenium import webdriver
except:
    os.system('python install pyautogui')
    os.system('python install keyboard')
    os.system('python install selenium')

client_host = '127.0.0.1'
client_port = 54321

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((client_host, client_port))

while True:
    print(f"Cliente UDP aguardando mensagens em {client_host}:{client_port}")
    data, addr = udp_socket.recvfrom(1024)
    command = data.decode('utf-8')
    print(f"Recebido de {addr}: {command}")
    if command == 'volume':
        for i in range(70):
            pyautogui.press('volumeup')
    elif command == 'luan':
        try:
            driver = webdriver.Edge()
            driver.get('https://youtu.be/qjjT960FYt4?si=kDPc1Xii6wbQWgxJ')
            sleep(3)
            pyautogui.press('Space')
            sleep(15)
        except:
            pass
    elif command == 'calc':
        os.system('calc')
