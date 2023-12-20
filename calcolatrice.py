import json

primoN=float(input("inserire numero"))
oper=input("inserire l'operatore (+,-,*,/,%)")
secN=float(input("inserire il secondo numero"))
mess={
    'primoNumero':primoN,
    'operazione':oper,
    'secondoNumero':secN
    }
mess=json.dumps(mess) #trasforma l'oggetto in una stringa
s=socket.socket
s.sendall(mess.encode("UTF-8"))
data=s.recv(1024)
print("risultato: ",data.decode())

data=cs.recv(1024)
# if len(data)==0:
while():
    if(oper=='+'):

    elif(oper=='-'):

    elif(oper=='*'):

    elif(oper=='/'):

    elif(oper=='%')

    else
