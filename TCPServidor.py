import socket, threading


connections = []

def trata_conexoes_de_usuarios(connection, address):
    # Pega a conexão do usuário e envia mensagens para outras conexões pre existentes

    while True:
        try:
            # recebe a mensagem do cliente
            msg = connection.recv(1024)

            if (msg.decode() == 'q'):
                break
            
            if (msg):
                print(f' Recebido de IP: {address[0]} Porta: {address[1]} -  a mensagem:   {msg}  ')
                
                userName = None
                msg = msg.decode()
     
                if msg.find('___')  != -1:
                    # Formata a mensagem para enviar para os clientes conectados
                    arrmsg = msg.split('___')
                    msg_to_send = f'{arrmsg[0]} >>> {arrmsg[1]}'
                    broadcast(msg_to_send, connection)

            else:
                remove_connection(connection)
                break

        except Exception as e:
            remove_connection(connection)
            break


def broadcast(message, connection):
    # Envia a mensagem para todos os clientes conectados

    # loop em todas as conexões
    for client_conn in connections:
        if client_conn != connection:
            try:
                client_conn.send(message.encode())
            except Exception as e:
                remove_connection(client_conn)


def remove_connection(conn):
    # Remove a conexão da lista de conexões

    if conn in connections:
        conn.close()
        connections.remove(conn)


def Main():
    #recebe as conexões e inicia uma thread pra tratar as mensagens dos usuarios

    LISTENING_PORT = 12000
    
    try:
        # Cria o servidor
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(1)

        print('Esperando mensagens...')
        
        while True:
            socket_connection, address = socket_instance.accept()

            # adicona a conexão para a lista de conexões
            connections.append(socket_connection)

            # Inicia uma nova thread
            threading.Thread(target=trata_conexoes_de_usuarios, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Error: {e}')
    finally:
        
        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)

        socket_instance.close()


if __name__ == "__main__":
    Main()