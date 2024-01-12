import json
import socket

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

#creazione socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    primoNumero=float(input("inserire numero"))
    operazione=input("inserire l'operatore (+,-,*,/,%)")
    secondoNumero=float(input("inserire il secondo numero"))
    message={
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero
        }
    message=json.dumps(message) #trasforma l'oggetto in una stringa
    sock.sendto(message.encode("UTF-8"),(SERVER_IP,SERVER_PORT))
    data=sock.recv(BUFFER_SIZE)
    print("risultato: ",data.decode())

    risp=input("vuoi fare altre operazioni 's'==si 'n'==no")
    if(risp=='n'):
        break


#chiusura del socket
sock.close()