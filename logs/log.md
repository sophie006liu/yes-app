8/19:

8/18 10 pm:

Last todo:
- read up on locking and threading
- explaining the output:
- note that the lock mechanism doesn't determine which thread acquires the lock first
so there's a nondeterministic order of operations

What happened:
Added a stopping condition for when producers finish

1) have a flag or counter that tracks the number of active producers
2) each producer decrements this counter when finished
3) consumer checks this flag and stop when the queue is empty

TODO:
- add a threading event so that consumer stopping is more efficient and avoid
unecessary work
-low priority: learn about reentrant lock, condition variables


8/18 2 am:

TODO:
-understand why the output is the way it is
-read up on locking and threading



