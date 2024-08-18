import os
import json
import threading

class Message_queue:
    def __init__(self, filename : str):
        self.queue = []
        self.filename = filename
        self.lock = threading.Lock()

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.queue = json.load(f)


    def enqueue(self, message):
        with self.lock:
            self.queue.append(message)
            print("after queue", self.queue)
            self._save_to_file()
        
    def dequeue(self):
        with self.lock:
            if not self.queue:
                print("empty")
                return None
            
            message = self.queue.pop(0)
            print("after dequeue", self.queue)
            self._save_to_file()
        
            return message

    def _save_to_file(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self.queue, f)
