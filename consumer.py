from message_queue import Message_queue
import threading, time
class Consumer(threading.Thread):
    def __init__(self, queue: Message_queue, name: str):
        super().__init__()
        self.queue = queue
        self.name = name

    def run(self):
        i = 0
        while True:
            message = self.queue.dequeue()
            if message:
                print(f"{self.name} consuming {message}")
            else:
                print(f"{self.name} found queue empty")
            time.sleep(2)

    def receive(self):
        return self.queue.dequeue()