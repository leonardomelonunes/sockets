import socket, threading, pickle
from model import Message
from utils import send_serialized, get_serialized_message, send_file_to_server, client_receive_save_file


# captura o nickname do usuário, pois será requisitado pelo servidor
nickname = input('Informe Seu Nome: ')


obj_to_send = Message()
obj_to_send.user = nickname


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 10000))


# escuta as mensagens enviadas pelo servidor
def receive():
    while True:
        try:
            data = client.recv(1024)
            if data:
                try:
                    data = get_serialized_message(client, data)
                    if data.message == 'NICK':
                        send_serialized(client, nickname)
                    else:
                        print(data.message)
                except:
                    client_receive_save_file(client, data)
            else:
                client.close()
                break
        except:
            client.close()
            break


# escuta os comandos do cliente (ex: enviar mensagens)
def write():
    while True:
        user_entry = input("")

        if user_entry == '-h':
            print('Os comandos disponíveis são:')
            print('-h Help')
            print('-q para Sair')
            print('-f para Enivar um arquivo')
            continue

        if user_entry == '-q':
            send_serialized(client, 'EXIT')
            break

        elif user_entry == '-f':
            send_file_to_server(client, nickname)

        else:
            message = f'{nickname}: {user_entry}'
            send_serialized(client, message)


threading.Thread(target=receive).start()
threading.Thread(target=write).start()