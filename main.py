from message_queue import Message_queue
from producer import Producer
from consumer import Consumer
import time, threading

def main():
    q = Message_queue('queue_data.json', 0)

    # Create and start multiple producers
    producer1 = Producer(q, "Producer 1")
    producer2 = Producer(q, "Producer 2")

    # Create and start multiple consumers
    consumer1 = Consumer(q, "Consumer 1")
    consumer2 = Consumer(q, "Consumer 2")

    producer1.start()
    producer2.start()

    consumer1.start()
    consumer2.start()

    # Wait for producers to finish
    producer1.join()
    producer2.join()

if __name__ == "__main__":
    main()
