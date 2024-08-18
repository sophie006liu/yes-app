from message_queue import Message_queue
import time, threading

class Producer(threading.Thread):
    def __init__(self, queue: Message_queue, name: str):
        super().__init__()
        self.queue = queue
        self.name = name

    def run(self):
        for i in range(5):
            message = f"Message {i} from {self.name}"
            print(f"{self.name} producing: {message}")
            self.send(message)
            time.sleep(1)

    def send(self, message):
        self.queue.enqueue(message)
