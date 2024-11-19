import threading
import time

def do_work():
    time.sleep(5)
    print ('Work finished')

threading.Thread.name = 'Main thread'

something_thread = threading.Thread(target=do_work,daemon=True)
something_thread.name = 'Daemon thread'
something_thread.start()

print(threading.Thread.name)
print(something_thread.name)

# STOP PROGRAM AFTER SOMETHING_THREAD HAS FINISHED WORK
# IF REMOVED, DAEMON PROPERTY WILL STOP SOMETHING_THREAD BEFORE IT HAS FINISHED WORK
while True:
    if something_thread.is_alive():
        continue
    else:
        break