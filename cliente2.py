#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
sexo = input()
idade = input()

messagem = str(nome + '/' + sexo + '/' + idade)


s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

if data == 'maioridade':
	print(nome,'já atingiu a maioridade')
else:
	print(nome,'não atingiu a maioridade')
