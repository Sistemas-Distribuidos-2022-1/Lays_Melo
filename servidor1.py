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
	
	nome,cargo,salario = data.split('/')

	salario = float(salario)
	
	if cargo == 'operador':
		salario *= 1.2
	if cargo == 'programador':
		salario *= 1.18
	
	data = str.encode(nome + '/' + cargo + '/' + str(salario))
	
	conn.sendall(data)
