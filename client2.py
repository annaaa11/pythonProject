# Клієнт:
#  receive_message(client) – отримує повідомлення від сервера
# та виводить на екран. Має використовуватись цикл while
# Основна програма:
#  підключитись до сервера
#  створити потік з функцією receive_message
#  запустити потік
#  попросити користувача ввести ім’я
#  створити цикл в якому користувач вводить повідомлення та
# надсилає на сервер

import socket
import json
import threading

 #отримує повідомлення від сервера
# та виводить на екран. Має використовуватись цикл while
def receive_message(client):
    while True:
        receive = client.recv(1024).decode()

        data = json.loads(receive)
        print()
        print(f"    {data['name']} відправив(ла) {data['message']}")

        if data['message'] == '':
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

receive_message = threading.Thread(target=receive_message, args=(client,))

receive_message.start()

name = input('Як вас звати? >>> ')

while True:
    message = input('Введіть повідомлення: ')

    data = {'name': name,
            'message': message}
    code = json.dumps(data)
    client.send(code.encode())

    if message == '':
        break


receive_message.join()
client.close()