from message_queue import Message_queue
import threading, time
class Consumer(threading.Thread):
    """
    Now bears the responsibility of detecting the stop condition
    """
    def __init__(self, queue: Message_queue, name: str):
        super().__init__()
        self.queue = queue
        self.name = name

    def run(self):
        while True:
            message = self.queue.dequeue()
            if message:
                print(f"{self.name} consuming {message}")
            elif self.queue.all_producers_done() and not self.queue.queue:
                print("All producers done")
                print("Check if if it prints an empty string", self.queue.queue)
                return
            else:
                print(f"{self.name} found queue empty")
            time.sleep(2)

    def receive(self):
        return self.queue.dequeue()