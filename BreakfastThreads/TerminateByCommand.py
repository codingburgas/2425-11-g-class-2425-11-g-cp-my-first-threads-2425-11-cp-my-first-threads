import time
import threading

counter = 0

def read_from_database():
    global counter
    while True:
        counter += 1
        time.sleep(1)

something_thread = threading.Thread(target=read_from_database,daemon=True)

something_thread.start()

print("1.Check reading status")
print("2.End program")

while True:
    match input("Choice: "):
        case "1":
            print(f"Database has read {counter} lines")
        case "2":
            break
        case _:
            "Wrong input"

print("Interrupting program")