import socket

IP="127.0.0.1"
PORTA=65432
DIM_BUFFER=1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP,PORTA))
    sock_server.listen()
    print(f"server in ascolto su {IP}:{PORTA}...")
    while True:
        sock_service, address_client=sock_server.accept()
        with sock_service as sock_client:
            dati=sock_client.recv(DIM_BUFFER).decode()
            print(f"ricevuto messaggio dal client {sock_client}:{dati}")
            sock_client.sendall("messaggio ricevuto dal server".encode())
                     