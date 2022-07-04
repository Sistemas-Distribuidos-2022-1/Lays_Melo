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
	nome,saldo_medio = data.split('/')
	
	saldo_medio = float(saldo_medio)
	
	if saldo_medio >= 0 and saldo_medio <= 200:
		data = 0
	elif saldo_medio > 200 and saldo_medio <= 400:
		data = saldo_medio*0.2
	elif saldo_medio > 400 and saldo_medio <= 600:
		data = saldo_medio*0.3
	elif saldo_medio > 600:
		data = saldo_medio*0.4
	
	data = str.encode(str(data))
	
	conn.sendall(data)
