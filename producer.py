from message_queue import Message_queue
import time, threading

class Producer(threading.Thread):
    """
    It has a name, it marks itself, unmarks itself
    Sends messages
    """

    def __init__(self, queue: Message_queue, name: str):
        super().__init__()
        self.queue = queue
        self.name = name

    def run(self):
        self.queue.producer_begin()
        for i in range(3):
            message = f"Message {i} from {self.name}"
            print(f"{self.name} producing: {message}")
            self.send(message)
            time.sleep(1)

        self.queue.producer_finished()
        print(f"{self.name} finished", f"Producer count = {self.queue.producer_count}")

    def send(self, message):
        self.queue.enqueue(message)
