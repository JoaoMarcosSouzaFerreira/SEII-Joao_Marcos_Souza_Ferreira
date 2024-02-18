import socket
import select

UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP

sock.bind((UDP_IP, IN_PORT)) # Associa o socket ao endereço e porta especificados


while True:

    data, addr = sock.recvfrom(1024) # Recebe os dados e o endereço do remetente
   
    if data:  # Verifica se há dados recebidos
       
        print "File name:", data # Imprime o nome do arquivo recebido
       
        file_name = data.strip() # Remove espaços em branco do nome do arquivo

   
    f = open(file_name, 'wb')  # Abre o arquivo no modo de escrita binária

   
    while True:
      
        ready = select.select([sock], [], [], timeout)  # Aguarda até que haja algo para ler no socket dentro do tempo limite
       
        if ready[0]: # Se há dados prontos para serem lidos no socket
           
            data, addr = sock.recvfrom(1024) # Recebe os dados
           
            f.write(data) # Escreve os dados no arquivo
        else:
           
            print "%s Finish!" % file_name # Se não houver mais dados para ler, imprime uma mensagem indicando que a transferência do arquivo foi concluída
           
            f.close() # Fecha o arquivo
           
            break # Sai do loop interno
