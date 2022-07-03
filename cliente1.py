#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
cargo = input()
salario = input()

messagem = str(nome + '/' + cargo + '/' + salario)


s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()
nome,cargo,salario = data.split('/') 

print('Nome: ', nome)
print('Cargo: ', cargo)
print('Salario reajustado: ', salario)
