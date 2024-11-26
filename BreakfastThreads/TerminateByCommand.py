import time
import threading

thread_stop = False
counter = 0

def read_from_database():
    global thread_stop
    global counter

    while True:
        if thread_stop:
            break

        counter += 1
        time.sleep(1)

something_thread = threading.Thread(target=read_from_database)

something_thread.start()

print("1.Check reading status")
print("2.End program")

while True:
    if thread_stop:
        break

    match input("Choice: "):
        case "1":
            print(f"Database has read {counter} lines")
        case "2":
            thread_stop = True
        case _:
            "Wrong input"

print("Stopping program")
print(f"Thread has finished with status code: {something_thread.is_alive()}")