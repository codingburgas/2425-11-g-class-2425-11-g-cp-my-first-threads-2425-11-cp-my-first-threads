import time

class Toast:
    def make_toast(self, quantity):

        time.sleep(1 * quantity)

        print("Toast thread")


    def jam_the_toast(self, quantity):

        time.sleep(1 * quantity)

        print("Jam thread")