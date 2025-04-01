# Сервер
#  send_message(from_client, to_client)
# o from_client – клієнт від якого отримуємо
# повідомлення
# o to_client – клієнт якому надсилаємо повідомлення
# У функції має використовуватись цикл while
# Основна програма:
#  створити сервер
#  підключити двох клієнтів
#  створити 2 потоки з функцією send_message
#  запустити поток

import socket
import json
import threading


def send_message(from_client, to_client):

    while True:

        message1 = from_client.recv(1024).decode()
        if message1:
            to_client.send(message1.encode())
            data1 = json.loads(message1)
            if data1['message'] == '': #конец разговора
                break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))

server.listen(2)
client1, addr1 = server.accept()
client2, addr2 = server.accept()

# створити 2 потоки з функцією send_message
send_message_12 = threading.Thread(target=send_message, args=(client1, client2))
send_message_21 = threading.Thread(target=send_message, args=(client2, client1))

send_message_12.start()
send_message_21.start()

send_message_12.join()
send_message_21.join()

client1.close()
client2.close()
server.close()