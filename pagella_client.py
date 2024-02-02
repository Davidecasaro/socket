import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22225
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP,SERVER_PORT))
    print(f"connesso a ({SERVER_IP}, {SERVER_PORT})")
    print("comandi disponibili: ")
    print("#list : per vedere i voti inseriti")
    print("#get /nomestudente : per richiedere i voti di uno studente")
    print("#set /nomestudente : per inserire uno studente")
    print("#put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente")
    print("#close : per chiudere la connessione ")
    while True:
        comando=input("digita il comando ")
        if(comando=="#close" or comando=="#list"):
            parametro=""
        else:
            parametro=input("digita il parametro ")
        message={
            'comando':comando,
            'parametro':parametro,
            }
        message=json.dumps(message) 
        sock.sendall(message.encode("UTF-8"))
        data=sock.recv(BUFFER_SIZE)

        ris=json.loads(data.decode())
        print(ris['valori'])

        
