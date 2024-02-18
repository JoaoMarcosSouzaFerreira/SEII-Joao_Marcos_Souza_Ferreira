import socket

HEADER = 64 #INFORMA QUE AS PRIMEIRAS MENSAGENS QUE SÃO TROCADAS TERÃO 64 BITS, REPRESENTANDO A QUANTIDADE DE BITS
PORT =  5050 #ESTA SERÁ A PORTA QUE COMUMENTE NÃO ESTÁ SENDO USADA PELO COMPUTADOR
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.15.79" #ESTE É O ATUAL SERVIDOR LOCAL QUE ESTOU USANDO
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.len(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello Word!")
input()
send("Hello Tim")
input()
send("Hello everyone!")
