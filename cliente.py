import socket, pickle
from tkinter import filedialog
from tkinter import Tk

class Mensagem(object):
    def __init__(self):
        self.usuario = ''
        self.msg = ''
        self.arquivo = ''

def Main():
    host = '127.0.0.1'
    port = 10000
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host,port))

    

    # cria o objeto
    objEnviar = Mensagem()
    objEnviar.usuario = input("Nome: ")
    objEnviar.msg = input("Mensagem: ")
    #abre uma tela para escolha do arquivo
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir = "/",title = "Escolha um arquivo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(file_path)
    file_b = open(file_path, 'rb')
    file_l = file_b.read()
    print(file_l)
    objEnviar.arquivo = file_l
            



    # serializa o objeto
    data_string = pickle.dumps(objEnviar)
    # envia o objeto serializado para o servidor
    mySocket.send(data_string)
    
    mySocket.close()

if __name__ == '__main__':
    Main()