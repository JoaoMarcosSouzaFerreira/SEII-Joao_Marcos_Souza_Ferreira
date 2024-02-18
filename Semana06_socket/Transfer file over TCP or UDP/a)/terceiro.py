import socket
import time
import sys


UDP_IP = "127.0.0.1" # Define o endereço IP e a porta do servidor UDP
UDP_PORT = 5005

buf = 1024 # Define o tamanho do buffer para leitura de dados

file_name = sys.argv[1] # Obtém o nome do arquivo a ser enviado a partir dos argumentos da linha de comando


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP

sock.sendto(file_name, (UDP_IP, UDP_PORT)) # Envia o nome do arquivo para o servidor

print "Sending %s ..." % file_name # Imprime uma mensagem indicando que o arquivo está sendo enviado


f = open(file_name, "r") # Abre o arquivo em modo de leitura

data = f.read(buf) # Lê os primeiros dados do arquivo

while(data):
    
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): # Envia os dados para o servidor via UDP
       
        data = f.read(buf) # Lê os próximos dados do arquivo
       
        time.sleep(0.02) # Dá um tempo curto para o receptor salvar os dados (opcional)


sock.close() # Fecha o socket

f.close()# Fecha o arquivo
