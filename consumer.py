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
        while not self.queue.stop_event.is_set():
            post = self.receive()
            if post:
                print(f"{self.name} responding to post: {post.content}")

            elif self.queue.all_producers_done() and not self.queue.queue:
                print("setting stop event")
                self.queue.stop_event.set()
                return
            else:
                print(f"{self.name} found queue empty")
            time.sleep(2)

    def receive(self):
        return self.queue.dequeue()