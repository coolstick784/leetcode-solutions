import time
class Foo:
    def __init__(self):
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        time.sleep(0.1)
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        time.sleep(0.2)
        printThird()
