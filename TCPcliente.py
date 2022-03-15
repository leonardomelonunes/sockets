import socket, threading

def trata_menssagens(connection):
    # Recebe a mensagem do servidor e exibe para o usuário
    
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            connection.close()
            break

def Main():

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        # Cria o socket e conecta com o servidor
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        # Cria uma thread para lidar com as mensagens
        threading.Thread(target=trata_menssagens, args=[socket_instance]).start()

        print('Conectado ao servidor de mensagens (evnie "q" - para sair) ')

        # pega o nome do usuário
        userName = None
        while userName == None:
            userName = input('Por favor digite seu nome:')

        
        while True:
            
            msg = input()

            if msg == 'q':
                socket_instance.send(msg.encode())
                break

            # envia a mensagem pro servidor
            msg = userName + '___' + msg
            socket_instance.send(msg.encode())

        # fecha a conexão com o servidor
        socket_instance.close()

    except Exception as e:
        print(f'Error {e}')
        socket_instance.close()


if __name__ == "__main__":
    Main()