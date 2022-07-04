#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT =  8500

#AF_INET = 
#SOCK_STREAM = 


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

print('Aguardando conexão de um cliente')
conn, ender = s.accept()

print('Conectado em', ender)

while True:
	data = conn.recv(1024)	
	
	
	if not data:
		print('Fechando conexão')
		conn.close()
		break	
	
	data = data.decode()
	nome,idade,tempo_servico= data.split('/')
	
	idade = int(idade)
	tempo_servico = int(tempo_servico)
	
	if idade >= 65 and tempo_servico >= 30:
		data = 'aposentado'
	elif idade >= 60 and tempo_servico >= 25:
		data = 'aposentado'
	else:
		data = 'nao aposentado'
		
	
	data = str.encode(str(data))
	
	conn.sendall(data)
