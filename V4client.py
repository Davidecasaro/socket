import socket,sys,random,os,time,threading,multiprocessing

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224
NUM_WORKERS=15

def genera_richieste(address,port):
    print(f"{threading.current_thread().name} execution time=", end_time_thread - start_time_thread)


if __name__=='__main__':
    start_time=time.time()
    threads=[threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time=time.time()

    print("total threads time=", end_time - start_time)