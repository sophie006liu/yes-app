the output is currently:

Producer 1 producing: Message 0 from Producer 1
after queue ['Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1']
Producer 2 producing: Message 0 from Producer 2
after queue ['Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2']
after dequeue ['Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2']
Consumer 1 consuming Message 1 from Producer 1
after dequeue ['Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2']
Consumer 2 consuming Message 1 from Producer 2
Producer 1 producing: Message 1 from Producer 1
Producer 2 producing: Message 1 from Producer 2
after queue ['Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1']
after queue ['Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2']
after dequeue ['Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2']
Consumer 1 consuming Message 2 from Producer 1
after dequeue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2']
Consumer 2 consuming Message 2 from Producer 2
Producer 1 producing: Message 2 from Producer 1
after queue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1']
Producer 2 producing: Message 2 from Producer 2
after queue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2']
Producer 1 producing: Message 3 from Producer 1
Producer 2 producing: Message 3 from Producer 2
after queue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1']
after queue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2']
after dequeue ['Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2']
Consumer 1 consuming Message 3 from Producer 1
after dequeue ['Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2']
Consumer 2 consuming Message 3 from Producer 2
Producer 1 producing: Message 4 from Producer 1
after queue ['Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1']
Producer 2 producing: Message 4 from Producer 2
after queue ['Message 4 from Producer 1', 'Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
after dequeue ['Message 4 from Producer 2', 'Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 1 consuming Message 4 from Producer 1
after dequeue ['Message 0 from Producer 1', 'Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 2 consuming Message 4 from Producer 2
after dequeue ['Message 0 from Producer 2', 'Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 1 consuming Message 0 from Producer 1
after dequeue ['Message 1 from Producer 1', 'Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 2 consuming Message 0 from Producer 2
after dequeue ['Message 1 from Producer 2', 'Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 2 consuming Message 1 from Producer 1
after dequeue ['Message 2 from Producer 1', 'Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 1 consuming Message 1 from Producer 2
after dequeue ['Message 2 from Producer 2', 'Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 2 consuming Message 2 from Producer 1
after dequeue ['Message 3 from Producer 1', 'Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 1 consuming Message 2 from Producer 2
after dequeue ['Message 3 from Producer 2', 'Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 2 consuming Message 3 from Producer 1
after dequeue ['Message 4 from Producer 1', 'Message 4 from Producer 2']
Consumer 1 consuming Message 3 from Producer 2
after dequeue ['Message 4 from Producer 2']
Consumer 2 consuming Message 4 from Producer 1
after dequeue []
Consumer 1 consuming Message 4 from Producer 2
empty
Consumer 2 found queue empty
empty
Consumer 1 found queue empty
empty
Consumer 2 found queue empty
empty

TODO:
-understand why the output is the way it is
-read up on locking and threading

