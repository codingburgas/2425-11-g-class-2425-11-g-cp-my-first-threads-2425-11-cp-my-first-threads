import threading
import time

class ProgressBar:
    def display_progress_bar(self, percentage):
        for i in range(0, percentage, 10):
            print("██", end="")

            time.sleep(1)

        for i in range(0, 100 - percentage, 10):
            print("░░", end="")

            time.sleep(1)

progress_bar = ProgressBar()

progress_bar_thread = threading.Thread(target=progress_bar.display_progress_bar, args=(10, ))

progress_bar_thread.start()