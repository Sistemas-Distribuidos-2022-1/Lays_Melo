#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
idade = input()
tempo_servico = input()


messagem = str(nome + '/' + idade + '/' + tempo_servico)

s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

if data == 'aposentado':
	print(nome, 'já pode se aposentar')
else:
	print(nome, 'não pode se aposentar')
