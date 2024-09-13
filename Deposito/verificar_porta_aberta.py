import socket

def verifica_porta(host,porta):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host,porta))

    if resultado == 0:
        print(f"Porta {porta} está ABERTA em {host}.")
    else:
        print(f"Porta {porta} está FECHADA em {host}.")
    sock.close()

host = "google.com"

verifica_porta(host,80)

