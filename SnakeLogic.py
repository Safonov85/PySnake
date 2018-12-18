import threading
from datetime import datetime

class SnakeLogic:

    def print_it():
        print(datetime.now())

    def start_timer():
        threading.Timer(5.0, print_it)
        threading.Timer.start()