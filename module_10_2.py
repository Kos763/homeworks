import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.wars = 100
        self.day = 0

    def run(self):
        print(f'{self.name} на нас напали!')

        while self.wars > 0:
            self.wars -= self.power
            self.day += 1
            time.sleep(1)
            if self.wars <= 0:
                break
            print(f"{self.name} сражается {self.day}, осталось {self.wars} воинов.")
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
