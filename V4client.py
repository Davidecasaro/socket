import socket
import json
from random import *
import sys
import os
import time
import threading
import multiprocessing
 
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224
NUM_WORKERS=15
BUFFER_SIZE=1024

def genera_richieste(SERVER_ADDRESS,SERVER_PORT):
    start_time_thread=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((SERVER_ADDRESS,SERVER_PORT))
        primoNumero=randint(1,10)
        secondoNumero=randint(1,10)
        ind=randint(0,4)
        vet=['+','-','*','/','%']
        operazione=vet[ind]

        message={
            'primoNumero':primoNumero,
            'operazione':operazione,
            'secondoNumero':secondoNumero
            }
        
        message=json.dumps(message) 
        sock_service.sendall(message.encode("UTF-8"))
        data=sock_service.recv(BUFFER_SIZE)
        print(f"risultato: ",data.decode())

        end_time_thread=time.time()
        print(f"{threading.current_thread().name} execution time=", end_time_thread-start_time_thread)


if __name__=='__main__':
    start_time=time.time()
    threads=[threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time=time.time()

    print("total threads time=", end_time-start_time)