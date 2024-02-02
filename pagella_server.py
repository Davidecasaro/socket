import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22225
BUFFER_SIZE=1024
pagella={   'Antonio Barbera': [   ['Matematica', 8, 1],
                           ['Italiano', 6, 1],
                           ['Inglese', 9.5, 0],
                           ['Storia', 8, 2],
                           ['Geografia', 8, 1]],
    'Giuseppe Gullo': [   ['Matematica', 9, 0],
                          ['Italiano', 7, 3],
                          ['Inglese', 7.5, 4],
                          ['Storia', 7.5, 4],
                          ['Geografia', 5, 7]],
    'Nicola Spina': [   ['Matematica', 7.5, 2],
                        ['Italiano', 6, 2],
                        ['Inglese', 4, 3],
                        ['Storia', 8.5, 2],
                        ['Geografia', 8, 2]]}
 

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print(f"server in ascolto su {SERVER_IP}:{SERVER_PORT}...")
    while True:
        sock_service, address_client=sock_server.accept()
        with sock_service as sock_client:
            while True:
                dati=sock_client.recv(BUFFER_SIZE).decode()
                if not dati:
                    break
                data=json.loads(dati)
                comando=data['comando']
                parametro=data['parametro']

                if(comando=="#list"):
                    messaggio="OK"
                    risultato=pagella

                elif(comando=="#get"):
                    _,ind=parametro.split("/")
                    if(pagella[ind] in pagella.keys()):
                        print("????",pagella[ind])
                        risultato=pagella[ind]
                        messaggio="OK"
                    else:
                        messaggio="KO"

                elif(comando=="#set"):
                    _,ind=parametro.split("/")

                    messaggio="OK"

                elif(comando=="#put"):
                    _,ind=parametro.split("/")
                    messaggio="OK"

                elif(comando=="#close"):
                    sock_service.close()

                dati={
                    "risposta":messaggio,
                    "valori":risultato,
                }

                sock_service.sendall(json.dumps(dati).encode())
                


