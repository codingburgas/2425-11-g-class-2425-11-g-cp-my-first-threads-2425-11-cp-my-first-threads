from ProgressBar import *
from Coffee import *
from Egg import *
from Bacon import *
from Toast import *
from Juice import *
import threading
import time

progress_counter = 0

coffee = Coffee()
egg = Egg()
bacon = Bacon()
toast = Toast()
jam = Toast()
juice = Juice()

coffee_thread = threading.Thread(target=Coffee.make_coffee(coffee,1))
eggs_thread = threading.Thread(target=Egg.make_eggs(egg,3))
bacon_thread = threading.Thread(target=Bacon.make_bacon(bacon,2))
toast_thread = threading.Thread(target=Toast.make_toast(toast,2))
jam_thread = threading.Thread(target=Toast.jam_the_toast(jam,1))
juice_thread = threading.Thread(target=Juice.make_juice(juice,1))

# PROGRESS BAR INSTANCE
progress_bar = ProgressBar()

# START AND DISPLAY COFFEE THREAD PROGRESS
coffee_thread.start()

coffee_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY EGGS THREAD PROGRESS
eggs_thread.start()

eggs_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY BACON THREAD PROGRESS
bacon_thread.start()

bacon_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY TOAST THREAD PROGRESS
toast_thread.start()

toast_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY JAM THREAD PROGRESS
jam_thread.start()

jam_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

# START AND DISPLAY JUICE THREAD PROGRESS
juice_thread.start()

juice_thread.join()

progress_counter += coffee_thread # TODO: Fix data type cast

progress_bar.display_progress_bar(progress_counter)

print("Breakfast is done!")