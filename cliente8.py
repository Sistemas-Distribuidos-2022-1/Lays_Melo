#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
saldo_medio = input()


messagem = str(nome + '/' + saldo_medio)

s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

print('Saldo médio:', saldo_medio)
print('Percentual de Crédito:',float(data))
