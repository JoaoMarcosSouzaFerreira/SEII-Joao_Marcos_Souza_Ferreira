import socket
import threading #PERMITE QUE O PROGRAMA EXECUTE OUTRA AÇÃO SEM QUE A ANTERIOR AINDA NÃO TENHA ACABADO

HEADER = 64 #INFORMA QUE AS PRIMEIRAS MENSAGENS QUE SÃO TROCADAS TERÃO 64 BITS, REPRESENTANDO A QUANTIDADE DE BITS
PORT =  5050 #ESTA SERÁ A PORTA QUE COMUMENTE NÃO ESTÁ SENDO USADA PELO COMPUTADOR
SERVER = "192.168.15.79" #ESTE É O ATUAL SERVIDOR LOCAL QUE ESTOU USANDO
ADDR = (SERVER, PORT) #CONECTANDO OS DOIS ENDEREÇOS
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CRIANDO UM NOVO SOCKET, ESPECIFICANDO O TIPO DO ENDEREÇO
server.bind(ADDR) #UNINDO OS ENDEREÇOS


def handle_client(conn, addr): #COMUNICAÇÃO ENTRE O CLIENTE E O SERVIDOR
    print ("[NEW CONECTION]{addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #GARANTE QUE NÃO ESTÃO BLOQUEANDO OUTRO CLIENTE
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
        conn.close()



    


def start():
    server.listen()
    while True:
        conn, addr = server.accept() #ESPERA POR UMA NOVA CONEXÃO COM O SERVIDOR, PERMITINDO QUE HAJA COMUNICAÇÃO
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()

