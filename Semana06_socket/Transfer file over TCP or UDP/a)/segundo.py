import socket

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket para controle de arquivos

sock_f.bind((TCP_IP, FILE_PORT)) # Associa o socket ao endereço e porta especificados

sock_f.listen(1) # Inicia a escuta do socket para conexões entrantes


sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket para dados

sock_d.bind((TCP_IP, DATA_PORT)) # Associa o socket ao endereço e porta especificados

sock_d.listen(1) # Inicia a escuta do socket para conexões entrantes


while True: # Loop infinito para aceitar conexões e processar dados
    
    conn, addr = sock_f.accept() # Aceita uma conexão no socket de controle de arquivos
   
    data = conn.recv(buf)  # Recebe os dados enviados pelo cliente
  
    if data:
        
        print "File name:", data # Imprime o nome do arquivo recebido
      
        file_name = data.strip() # Remove espaços em branco do nome do arquivo

    
    f = open(file_name, 'wb') # Abre o arquivo no modo de escrita binária

   
    conn, addr = sock_d.accept()  # Aceita uma conexão no socket de dados
    
    while True:
        
        data = conn.recv(buf) # Recebe os dados do cliente
        
        if not data: # Verifica se não há mais dados a receber
            break
        
        f.write(data) # Escreve os dados recebidos no arquivo

    
    print "%s Finish!" % file_name # Imprime uma mensagem indicando que a transferência do arquivo foi concluída
   
    f.close()  # Fecha o arquivo
