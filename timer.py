import threading

time=0

def timerx(p):
    global time
    time += 1
    print(time)
    timer=threading.Timer(1, timerx, args=[p])
    timer.start()
    
    if time==p :
        timer.cancel()
        
timerx(5)
