from ProgressBar import *
from Coffee import *
from Egg import *
from Bacon import *
from Toast import *
from Juice import *
import threading

progress_counter = 0

coffee = Coffee()
egg = Egg()
bacon = Bacon()
toast = Toast()
jam = Toast()
juice = Juice()

coffee.quantity = 1
egg.quantity = 1
bacon.quantity = 1
toast.quantity = 1
jam.quantity = 1
juice.quantity = 1

coffee_thread = threading.Thread(target=Coffee.make_coffee(coffee,coffee.quantity),name= "Coffee thread", daemon=True)
eggs_thread = threading.Thread(target=Egg.make_eggs(egg,egg.quantity), name= "Eggs thread")
bacon_thread = threading.Thread(target=Bacon.make_bacon(bacon,bacon.quantity), name= "Bacon thread")
toast_thread = threading.Thread(target=Toast.make_toast(toast,toast.quantity), name= "Toast thread")
jam_thread = threading.Thread(target=Toast.jam_the_toast(jam,jam.quantity), name= "Jam thread")
juice_thread = threading.Thread(target=Juice.make_juice(juice,juice.quantity), name= "Juice thread")

# PROGRESS BAR INSTANCE
progress_bar = ProgressBar()

# START AND DISPLAY COFFEE THREAD PROGRESS

coffee_thread.start()
#coffee_thread.join()

#progress_counter += coffee.quantity

#progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY EGGS THREAD PROGRESS
eggs_thread.start()
#eggs_thread.join()

#progress_counter += egg.quantity

# START AND DISPLAY BACON THREAD PROGRESS
bacon_thread.start()
#bacon_thread.join()

#progress_counter += bacon.quantity

#progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY TOAST THREAD PROGRESS
toast_thread.start()
#toast_thread.join()

#progress_counter += toast.quantity

#progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY JAM THREAD PROGRESS
jam_thread.start()
#jam_thread.join()

#progress_counter += jam.quantity

#progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY JUICE THREAD PROGRESS
juice_thread.start()
#juice_thread.join()

#progress_counter += juice.quantity

#progress_bar.display_progress_bar(progress_counter)

print("Breakfast is done!")