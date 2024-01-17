import socket
import threading

# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем хост и порт для сервера
host = '127.0.0.1'
port = 12345

# Привязываем сокет к указанному хосту и порту
server_socket.bind((host, port))

# Слушаем входящие соединения
server_socket.listen()

# Список клиентов
clients = []


# Функция для обработки сообщений от клиентов
def handle_client(client_socket, addr):
    while True:
        try:
            # Принимаем сообщение от клиента
            message = client_socket.recv(1024).decode('utf-8')

            # Рассылаем сообщение всем клиентам
            for client in clients:
                client.send(f'{addr[0]}:{addr[1]} says: {message}'.encode('utf-8'))
        except:
            # Удаляем клиента из списка при возникновении ошибки
            clients.remove(client_socket)
            client_socket.close()
            break


# Принимаем входящие соединения
while True:
    client_socket, addr = server_socket.accept()

    # Добавляем клиента в список
    clients.append(client_socket)

    # Запускаем отдельный поток для обработки сообщений от клиента
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
