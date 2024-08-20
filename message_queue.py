import os
import json
import threading
import heapq
from post import Post

class Message_queue:
    def __init__(self, filename: str, producer_count: int):
        self.queue = []
        self.filename = filename
        self.lock = threading.Lock()
        self.producer_count = producer_count
        self.producer_count_lock = threading.Lock()
        self.stop_event = threading.Event()
        self.counter = 0 

        if os.path.exists(self.filename) and self.is_json_file_not_empty(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.queue = [(-priority, count, Post(**post)) for priority, count, post in data['queue']]

    def enqueue(self, message, priority=0):
        with self.lock:
            self.counter += 1
            heapq.heappush(self.queue, (-priority, self.counter, message))
            self._save_to_file()

    def dequeue(self):
        with self.lock:
            if not self.queue:
                return None

            priority, count, message = heapq.heappop(self.queue)
            self._save_to_file()

            return message

    def producer_begin(self):
        with self.producer_count_lock:
            self.producer_count += 1

    def producer_finished(self):
        with self.producer_count_lock:
            self.producer_count -= 1

    def all_producers_done(self):
        return self.producer_count == 0

    def is_json_file_not_empty(self, filename):
        if not os.path.exists(filename):  
            return False
    
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
                return bool(data)  
            except json.JSONDecodeError: 
                return False

    def _save_to_file(self) -> None:
        with open(self.filename, 'w') as f:
            data = {
                'queue': [(-priority, count, post.__dict__) for priority, count, post in self.queue]
            }
            json.dump(data, f)
