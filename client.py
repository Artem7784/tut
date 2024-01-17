import socket
import threading

# Создаем клиентский сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем хост и порт сервера
host = '127.0.0.1'
port = 12345

# Подключаемся к серверу
client_socket.connect((host, port))

# Функция для отправки сообщений серверу
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Функция для приема сообщений от сервера
def receive_message():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

# Запускаем отдельные потоки для отправки и приема сообщений
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
