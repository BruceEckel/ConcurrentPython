Communicating Sequential Processes
==================================

The biggest problem in concurrency is that tasks can interfere with each other.
There are certainly other problems, but this is the biggest. This interference
generally appears in the form of two tasks attempting to read and write the
same data storage. Because the tasks run independently, you can't know which
one has modified the storage so the data is effectively corrupt. This is the
problem of *shared-memory concurrency*.

You will see later in this book that there are concurrency strategies which
attempt to solve the problem by locking the storage while one task is using
it so the other task is unable to read or write that storage. Although there is
not yet a conclusive proof, some people believe that this dance is so tricky and
complicated that it's impossible to write a correct program of any complexity
using shared-memory concurrency.

One solution to this problem is to altogether eliminate the possibility of
shared storage. Each task is isolated, and the only way to communicate with
other tasks is through controlled channels which safely pass data from one task
to another. This is the general description of *communicating sequential
processes* (CSP). The *sequential* term means that, within any process, you can
effectively ignore the fact that you are working within a concurrent world and
program as you normally do, sequentially from beginning to end. By defending you
from shared-memory pitfalls, CSP allows you to think more simply about the
problem you're solving.

We shall explore a number of strategies that implement CSP, but the easiest
place to start is probably Python's built-in `multiprocessing` module.
