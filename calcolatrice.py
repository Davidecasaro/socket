import json

primoNumero=float(input("inserire numero"))
operazione=input("inserire l'operatore (+,-,*,/,%)")
secondoNumero=float(input("inserire il secondo numero"))
message={
    'primoNumero':primoNumero,
    'operazione':operazione,
    'secondoNumero':secondoNumero
    }
message=json.dumps(message) #trasforma l'oggetto in una stringa
s=socket.socket
s.sendall(message.encode("UTF-8"))
data=s.recv(1024)
print("risultato: ",data.decode())

data=cs.recv(1024)
# if len(data)==0:
while():
    if(operazione=='+'):

    elif(operazione=='-'):

    elif(operazione=='*'):

    elif(operazione=='/'):

    elif(operazione=='%')

    else
