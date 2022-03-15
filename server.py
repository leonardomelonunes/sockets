import socket, pickle

class Mensagem(object):
    def __init__(self):
        self.usuario = ''
        self.msg = ''
        self.arquivo = ''

def Main():
    host = "0.0.0.0"
    port = 10000
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.bind((host,port))
    socketTCP.listen(1)
    print('Servidor TCP: {}:{}'.format(host,port))

    conn, addr = socketTCP.accept()
    print ("Conexão realizada por: " + str(addr))
    
    #recebe a mensagem do usuário
    data = conn.recv(4096)
    #mostra a mensagem serializada
    print (data)
    #desserializa a mensagem recebida, disponibilizando o objeto novamente na memoria
    objetoRecebido = pickle.loads(data)
    #mostra os dados do objeto
    print ('Nome: ' + objetoRecebido.usuario)
    print ('Mensagem: ' + objetoRecebido.msg)
    print ('arquivo: ' + objetoRecebido.arquivo)

    conn.close()

if __name__ == '__main__':
    Main()