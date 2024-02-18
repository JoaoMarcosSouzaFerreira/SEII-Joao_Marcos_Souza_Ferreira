import socket # Importa o módulo 'socket' para lidar com comunicação em rede
import sys # Importa o módulo 'sys' para acessar argumentos da linha de comando

TCP_IP = "127.0.0.1" # Define o endereço IP do servidor TCP/IP
FILE_PORT = 5005 # Define a porta para o envio de arquivo
DATA_PORT = 5006 # Define a porta para o envio de dados
buf = 1024 # Define o tamanho do buffer para leitura de dados
file_name = sys.argv[1] # Obtém o nome do arquivo a ser enviado a partir dos argumentos da linha de comando


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP/IP
    sock.connect((TCP_IP, FILE_PORT))  # Estabelece conexão com o servidor na porta FILE_PORT
    sock.send(file_name) # Envia o nome do arquivo para o servidor
    sock.close()  # Fecha o socket

    print "Sending %s ..." % file_name # Imprime uma mensagem indicando que o arquivo está sendo enviado

    f = open(file_name, "rb")  # Abre o arquivo em modo de leitura binária
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um novo socket TCP/IP
    sock.connect((TCP_IP, DATA_PORT))  # Estabelece conexão com o servidor na porta DATA_PORT
    data = f.read() # Lê os dados do arquivo
    sock.send(data) # Envia os dados para o servidor

finally:
    sock.close() # Fecha o socket
    f.close() # Fecha o arquivo
