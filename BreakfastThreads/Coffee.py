import time

class Coffee:

    def make_coffee(self,quantity):

        time.sleep(1 * quantity)

        print("Coffee thread")