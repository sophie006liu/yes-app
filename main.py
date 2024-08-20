from message_queue import Message_queue
from producer import Producer
from consumer import Consumer
import time, threading

def main():
    q = Message_queue('queue_data.json', 0)

    producer1 = Producer(q, "Producer 1", 3, 0)
    producer2 = Producer(q, "Producer 2", 3, 1)
    producer3 = Producer(q, "Producer 3", 3, 2)

    consumer1 = Consumer(q, "Consumer 1")
    consumer2 = Consumer(q, "Consumer 2")

    producer1.start()
    producer2.start()
    producer3.start()

    consumer1.start()
    consumer2.start()

    # Wait for producers to finish
    producer1.join()
    producer2.join()

if __name__ == "__main__":
    main()
