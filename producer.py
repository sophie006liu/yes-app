from message_queue import Message_queue
from post import Post
import time, threading

class Producer(threading.Thread):
    """
    Producer class that produces posts with a given priority.
    """

    def __init__(self, queue: Message_queue, name: str, num_posts: int, priority: int = 0):
        super().__init__()
        self.queue = queue
        self.name = name
        self.priority = priority
        self.num_posts = num_posts

    def run(self):
        self.queue.producer_begin()
        for i in range(self.num_posts):
            post = Post(post_id=f"{self.name}_{i}", content=f"Post {i} from {self.name}")
            print(f"{self.name} posting with priority {self.priority}: {post.content}")
            self.send(post)
            time.sleep(1)

        self.queue.producer_finished()
        print(f"{self.name} finished. Producer count = {self.queue.producer_count}")

    def send(self, post):
        self.queue.enqueue(post, priority=self.priority)
