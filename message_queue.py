import os
import json
import threading

class Message_queue:
    def __init__(self, filename: str, producer_count: int):
        self.queue = []
        self.filename = filename
        self.lock = threading.Lock()
        self.producer_count = producer_count
        self.producer_count_lock = threading.Lock()

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.queue = json.load(f)

    def enqueue(self, message):
        with self.lock:
            self.queue.append(message)
            self._save_to_file()
        
    def dequeue(self):
        with self.lock:
            if not self.queue:
                return None
            
            message = self.queue.pop(0)
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

    def _save_to_file(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self.queue, f)
