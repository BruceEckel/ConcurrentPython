Introduction
============

> "Double, double toil and trouble; Fire burn and caldron bubble."---William Shakespeare, *MacBeth*

The only justification for concurrency is that your program doesn't run fast
enough. There are a few languages designed to make concurrency relatively
effortless---at least, their particular flavor of concurrency, which might or might
not fit your needs---but these are not yet the most popular programming languages.
Python does what it can to make concurrency "Pythonic," but you must still work
within the limitations of a language that wasn't designed around concurrency.

You can be thoroughly fluent in Python and know little to nothing about
concurrency. Indeed, for this book I expect those exact credentials. This means,
however, that diving into concurrency is a test of patience. You, a competent
programmer, must suffer the indignity of being thrown back to "beginner" status,
and learn new fundamental concepts (when, by this time, you thought you were
pretty accomplished at this programming thing).

I say all this to give you one last chance to rethink your strategy and consider
whether there might be some other way to make your program run faster. There are
many simpler approaches:

*   Faster hardware is probably much cheaper than programmer time.

*   Have you upgraded to the latest version of Python? That often produces
    speed improvements.

*   Use a profiler to discover your speed bottleneck, and see if you can change
    an algorithm. For example, sometimes the choice of data structure makes all
    the difference.

*   Try using [Cython](http://cython.org/) on functions with performance bottlenecks.

*   See if your program will run on [PyPy](http://pypy.org/).

*   If your bottlnecks are math-intensive, consider [Numba](http://numba.pydata.org/).

*   Search the Internet for other performance approaches.

If you jump right to concurrency without exploring these other approaches first,
you might still discover that your problem is dominated by one of these issues and
you must use them anyway. You might also need to use them in addition to a concurrency
approach.

What Does the Term *Concurrency* Mean?
--------------------------------------

As a non-concurrent programmer, you think in linear terms: A program runs from
beginning to end, performing all its intermediate steps in sequence. This is the
easiest way to think about programming.

Concurrency breaks a program into pieces, typically called *tasks*. These tasks
are, as much as possible, run independently of each other, with the hope that
the whole program will now run faster.

That's concurrency in a nutshell: Independently-running tasks.

At this point your brain should be exploding with questions:

*   How do I start a task?

*   How do I stop a task?

*   How do I get information into a task?

*   How do I get results from a task?

*   What mechanism drives the tasks?

*   How do tasks fail?

*   Can tasks communicate with each other?

*   What happens if two tasks try to use the same piece of storage?

These are not naive---they are precisely the questions you must ask to
understand concurrency. There is no one answer to any of them. In fact, these
questions distinguish the different concurrency strategies.

The term "concurrency" is often defined inconsistently in the literature. One of
the more common distinctions declares concurrency to be when all tasks are being
driven by a single processor, vs *parallelism* where tasks are distributed among
multiple processors. There are (mostly historical) reasons for this difference,
but in this book I relegate "the number of processors driving the tasks" as one
of the many variables involved with the general problem of concurrency.

Concurrency is initially overwhelming precisely because it is a general goal
("make a program faster using tasks") with a myriad of strategies to achieve
that goal---and more strategies regularly appear. The overwhelm diminishes when
you understand it from the perspective of different competing strategies for the
same problem.

This book takes the pragmatic approach of only giving you what you need to solve
your problem, starting with the simplest strategies first. It's not
*possible* to understand everything about concurrency, so requiring that you do
so in order to implement the simplest approach necessary to solve your problem
is unreasonable and impractical.

- What does "asynchronous" mean?
  * When a function finishes vs. when it returns
  * Again, not something you're used to thinking about
  * Because the answer has always been: "at the same time"

> [NOTE] The following has been pasted directly from *On Java 8* and has yet
to be chopped up and edited to make it appropriate for this book. Much may not
survive.

Up to this point we've been programming in a fashion much like the
*stream-of-consciousness* narrative device in literature: first one thing
happens, then the next. We're in complete control of all the steps and the order
they occur. It would be very surprising if we were to set a value to 5, then at
some point later come back and find it was 47.

We now enter the strange world of concurrency, where this result is not
surprising at all. Everything you're comfortable believing is no longer
reliable. It might work and it might not. Most likely it will work under some
conditions and not in others, and you'll have to know and understand these
situations in order to determine what works.

As an analogy, your normal life takes place in the world of Newtonian Mechanics.
Objects have mass: they fall and transfer their momentum. Wires have resistance,
and light travels in straight lines. But if you enter the world of the very
small, very hot, very cold or very massive (where we can't exist) things change.
We can't tell whether something is a particle or a wave, light is affected by
gravity, and some things become superconductors.

Rather than a single stream-of-consciousness narrative, we're inside a spy novel
that has numerous stories running at the same time, one for each character. One
spy leaves microfilm under a special rock, and when the second spy comes to
retrieve the package, it might already have been taken by a third spy. But this
particular novel doesn't neatly tie things up; you can easily get to
the end and never figure out what happens.

Building concurrent applications is much like the game
(Jenga)[https://en.wikipedia.org/wiki/Jenga], where every time you pull out a
block and place it on the tower, the whole thing can come crashing down. Every
tower, and every application, is unique, with its own requirements. What you
learn from building one system might not apply to the next one.

This chapter is a very basic introduction to concurrency. Although I use the
most modern Python tools available to demonstrate the principles, the chapter is
far from a comprehensive treatment of the topic. My goal is to give you enough
of the fundamentals that you can grasp the complexity---and danger---of the
issues, to engender a healthy respect for the difficulty of wading into these
shark-infested waters.


The Terminology Problem
-----------------------

The terms *concurrent*, *parallel*, *multitasking*, *multiprocessing*,
*multithreading*, *distributed systems* (and probably others) are used in
numerous conflicting ways throughout programming literature, and are often
conflated. After pointing this out in his 2016 presentation [From Concurrent to
Parallel](https://www.youtube.com/watch?v=NsDE7E8sIdQ), Brian Goetz suggests a
reasonable dichotomy:

+   Concurrency is about correctly and efficiently controlling access to
    shared resources.

+   Parallelism uses additional resources to produce an answer faster.

These are good definitions, but there are decades of confusion-producing history
that fight against fixing the problem. In general, when people use the word
"concurrency," they mean "everything, the entire mess," and I'll probably fall
into that practice myself in many places---indeed, most books use the word in the title.

Concurrency often means "more than one task is making progress," while
parallelism almost always means "more than one task is executing
simultaneously." You can immediately see the problem with these definitions:
parallelism also has more than one task "making progress." The distinction is
the details, in exactly *how* that "progress" is happening. Also, the overlap: a
program written for parallelism can still sometimes run on a single processor,
while some concurrent-programming systems can take advantage of more than one
processor.

Here's another approach, writing the definitions around where the slowdown
occurs:

*Concurrency*

: Accomplishing more than one task at the same time. One task doesn't need to
complete before you start working on other tasks. Concurrency solves problems
where *blocking* occurs---where a task can't progress further until something
outside its control changes; the most common example is I/O, where a task must
wait for some input (in which case it is said to be *blocked*). A problem like
this is said to be *I/O bound*.

*Parallelism*

: Accomplishing more than one task *in multiple places* at the same time. This
solves so-called *compute-bound* problems, where a program can run faster if you
split it into multiple parts and run those different parts on different
processors.

The reason the terminology is confusing is shown in the definitions above: the
core of both is "accomplishing more than one task at the same time." Parallelism
adds distribution across multiple processors. More importantly, the two solve
different types of problems: taking an I/O-bound problem and parallelizing might
not do you any good because the problem is not overall speed, it's blocking. And
taking a compute-bound problem and trying to solve it using concurrency on a
single processor might be a similar waste of time. Both approaches try to
accomplish more in less time, but the way they achieve speedup is different, and
depends upon constraints imposed by the problem.

A major reason that the two concepts get mixed together is that many programming
languages including Python use the same mechanism---the *thread*---to implement
both concurrency and parallelism.

We can even try to add more granularity to the definitions (however, this is not
standardized terminology):

+   **Purely Concurrent**: Tasks still run on a single CPU. A purely
    concurrent system produces results faster than a sequential system, but
    doesn't run any faster if there are more processors.

+   **Concurrent-Parallel**: Using concurrency techniques, the resulting
    program takes advantage of more processors and produces results faster.

+   **Parallel-Concurrent**: Written using parallel programming techniques,
    the resulting program can still run if there is only a single processor
    (Python `Stream`s are a good example).

+   **Purely Parallel**: Won't run unless there is more than one processor.

This might be a useful taxonomy in some situations.

Language and library support for concurrency seem like perfect candidates for
the term [Leaky Abstraction](https://en.wikipedia.org/wiki/Leaky_abstraction).
The goal of an abstraction is to "abstract away" pieces that are not essential
to the idea at hand, to shield you from needless detail. If the abstraction is
leaky, those pieces and details keep re-asserting themselves as important,
regardless of how much you try to hide them.

I've started to wonder whether there's really any abstraction at all---when
writing these kinds of programs you are never shielded from any of the
underlying systems and tools, even details about how the CPU cache works.
Ultimately, if you've been very careful, what you create will work in a
particular situation, but it won't work in other situations. Sometimes the
difference is the way two machines are configured, or the estimated load for the
program. This is not specific to Python per se---it is the nature of concurrent
and parallel programming.

You might argue that a [pure
functional](https://en.wikipedia.org/wiki/Purely_functional) language doesn't
have these restrictions. Indeed, a pure functional language solves a large
number of concurrency problems, so if you are tackling a difficult concurrency
problem you might consider writing that portion in a pure functional language.
But ultimately, if you write a system that has, for example, a queue somewhere,
if things aren't tuned right and the input rate either isn't estimated correctly
or throttled (and throttling means different things and has different impacts in
different situations), that queue will either fill up and block, or overflow. In
the end, you must understand all the details, and any issue can break your
system. It's a very different kind of programming.

### A New Definition of Concurrency

For decades, I have periodically grappled with concurrency in various forms,
and one of the biggest challenges has always been simply defining it. While
writing this chapter, I finally had an insight which I think captures it:

> Concurrency is a collection of performance techniques focused on the reduction
> of waiting.

This is actually a rather dense statement, so I'll break it down:

+   It's a *collection*: there are many different approaches to solving the
    problem. This is one of the issues that makes defining concurrency so
    challenging, because the techniques vary all over the place.

+   These are *performance techniques*: That's it. The whole point of
    concurrency is to get your program to run faster. In Python, concurrency
    is very tricky and difficult, so absolutely do not use it unless you
    have a significant performance problem---and even then, use the easiest
    approach that produces the performance you need, because concurrency
    rapidly becomes unmanageable.

+   The "reduction of waiting" part is important and subtle. Regardless of (for
    example) how many processors you are running on, you can only produce a
    benefit when some kind of waiting is taking place. If you ask for I/O and
    instantly get a result, there's no delay to take advantage of. If you are
    running multiple tasks on multiple processors and each is running at full
    capacity and no task is waiting on any other, there's no point in trying
    to improve your throughput. The only opportunity for concurrency is if
    some part of your program is forced to wait for some reason, and that
    waiting can appear in many forms---which explains why there are so many
    different approaches to concurrency.

It's worth emphasizing that the effectiveness of this definition hinges on the
word *waiting*. If nothing is waiting there's no opportunity for speedups. And
if something is waiting, there are numerous approaches to speeding things up and
these depend on multiple factors including the configuration of the system where
it's running, the type of problem you're solving, and any number of other
issues.

Concurrency Superpowers
-----------------------

Imagine you're inside a science-fiction movie. You must search a tall building
for a single item that is carefully and cleverly hidden in one of the ten
million rooms of the building. You enter the building and move down a corridor.
The corridor divides.

By yourself it will take a hundred lifetimes to accomplish this task.

Now suppose you have a strange superpower. You can split yourself in two, and
send one of yourself down one corridor while you continue down the other. Every
time you encounter a divide in a corridor or a staircase to the next level, you
repeat this splitting-in-two trick. Eventually there is one of you for every
terminating corridor in the entire building.

Each corridor contains a thousand rooms. Your superpower is getting stretched a
little thin, so you only make 50 of yourself to search the rooms in parallel.

Once a clone enters a room, it must search through all the cracks and hidden
pockets of the room. It switches to a second superpower. It divides into a
million nanobots, each of which flies or crawls to some unseen spot in the room.
You don't understand this power---it just works, once you start it. Under their
own control, the nanobots go, search the room and come back and reassemble into
you, and suddenly, somehow, you just know whether the item is in the room or
not.

I'd love to be able to say, "Your superpower in the science-fiction movie?
That's what concurrency is." That it's as simple as splitting yourself in two
every time you have more tasks to solve. The problem is that any model we use
to describe this phenomenon ends up being a leaky abstraction.

Here's one of those leaks: In an ideal world, every time you cloned yourself,
you would also duplicate a hardware processor to run that clone. But of course
that isn't what happens---you actually might have four or eight processors on
your machine (typical when this was written). You might also have more, and
there are still lots of situations where you have only one processor. In the
abstraction under discussion, the way physical processors are allocated not only
leaks through but can even dominate your decisions.

Let's change something in our science-fiction movie. Now when each clone
searcher eventually reaches a door they must knock on it and wait until someone
answers. If we have one processor per searcher, this is no problem---the
processor just idles until the door is answered. But if we only have eight
processors and thousands of searchers, we don't want a processor to be idle
just because a searcher happens to be blocked, waiting for a door to be
answered. Instead, we want that processor applied to a searcher where it can do
some real work, so we need mechanisms to switch processors from one task to
another.

Many models are able to effectively hide the number of processors and allow you
to pretend you have a very large number. But there are situations where this
breaks down, when you must know the number of processors so you can work
around that number.

One of the biggest impacts depends on whether you have a single processor or
more than one. If you only have one processor, then the cost of task-switching
is also borne by that processor, and applying concurrency techniques to your
system can make it run *slower*.

This might make you decide that, in the case of a single processor, it never
makes sense to write concurrent code. However, there are situations where the
*model* of concurrency produces much simpler code and it's actually worth having
it run slower to achieve that.

In the case of the clones knocking on doors and waiting, even the single-
processor system benefits from concurrency because it can switch from a task
that is waiting (*blocked*) to one that is ready to go. But if all the tasks
can run all the time, then the cost of switching is going to slow everything
down, and in that case concurrency usually only makes sense if you *do* have
multiple processors.

Suppose you are trying to crack some kind of encryption. The more workers trying
to crack it at the same time, the better chance you have of finding the answer
sooner. Here, each worker can constantly use as much processor time as you can
give it, and the best situation is when each worker has their own processor---in
this case (a compute-bound problem), you should write the code so you *only*
have as many workers as you have processors.

In a customer-service department that takes phone calls, you only have a certain
number of people, but you can have lots of phone calls. Those people (the
processors) must work on one phone call at a time until it is complete, and
extra calls must be queued.

In the fairy tale of "The Shoemaker and the Elves," the shoemaker had too much
work to do and when he was asleep, a group of elves came and made shoes for him.
Here the work is distributed but even if you have a large number of
physical processors the bottleneck is in the limitation of building certain
parts of the shoe---if, for example, the sole takes the longest to make, that
will limit the rate of shoe creation and change the way you design your
solution.

Thus, the problem you're trying to solve drives the design of the solution.
There's the lovely abstraction of breaking a problem into subtasks that "run
independently," then there's the reality of how it's actually going to happen.
The physical reality keeps intruding upon, and shaking up, that abstraction.

That's only part of the problem. Consider a factory that makes cakes. We've
somehow distributed the cake-making task among workers, but now it's time for a
worker to put their cake in a box. There's a box sitting there, ready to receive
a cake. But before the worker can put the cake into the box, another worker
darts in and puts *their* cake in the box instead! Our worker is already putting
the cake in, and bam! The two cakes are smashed together and ruined. This is the
common "shared memory" problem that produces what we call a *race condition*,
where the result depends on which worker can get their cake in the box first
(you typically solve the problem using a locking mechanism so one worker can
grab the box first and prevent cake-smashing).

The problem occurs when tasks that execute "at the same time" interfere with
each other. This can happen in such a subtle and occasional manner it's probably
fair to say that concurrency is "arguably deterministic but effectively
nondeterministic." That is, you can hypothetically write concurrent programs
that, through care and code inspection, work correctly. In practice, however,
it's much more common to write concurrent programs that only appear to work, but
given the right conditions, will fail. These conditions might never actually
occur, or occur so infrequently you never see them during testing. In fact, it's
often impossible to write test code to generate failure conditions for your
concurrent program. The resulting failures often only occur occasionally, and as
a result they appear in the form of customer complaints. This is one of the
strongest arguments for studying concurrency: If you ignore it, you're likely to
get bitten.

Concurrency thus seems fraught with peril, and if that makes you a bit fearful,
this is probably a good thing. Although Python makes large improvements in
concurrency, there are still no safety nets like compile-time verification or
checked exceptions to tell you when you make a mistake. With concurrency, you're
on your own, and only by being knowledgeable, suspicious and aggressive can you
write reliable concurrent code in Python.


Concurrency is for Speed
------------------------

After hearing about the pitfalls of concurrent programming, you may rightly be
wondering if it's worth the trouble. The answer is "no, unless your program
isn't running fast enough." And you'll want to think carefully before deciding
it isn't. Do not casually jump into the well of grief that is concurrent
programming. If there's a way to run your program on a faster machine or if you
can profile it and discover the bottleneck and swap in a faster algorithm in
that spot, do that instead. Only if there's clearly no other choice should you
begin using concurrency, and then only in isolated places.

The speed issue sounds simple at first: If you want a program to run faster,
break it into pieces and run each piece on a separate processor. With our
ability to increase clock speeds running out of steam (at least for conventional
chips), speed improvements are appearing in the form of multicore processors
rather than faster chips. To make your programs run faster, you'll have to learn
to take advantage of those extra processors, and that's one thing that
concurrency gives you.

If you have a multiprocessor machine, multiple tasks can be distributed across
those processors, which can dramatically improve throughput. This is often the
case with powerful multiprocessor Web servers, which can distribute large
numbers of user requests across CPUs in a program that allocates one thread per
request.

However, concurrency can often improve the performance of programs running on a
*single* processor. This can sound a bit counterintuitive. If you think about
it, a concurrent program running on a single processor should actually have
*more* overhead than if all the parts of the program ran sequentially, because
of the added cost of the *context switch* (changing from one task to another).
On the surface, it would appear cheaper to run all the parts of the program as a
single task and save the cost of context switching.

The issue that can make a difference is *blocking*. If one task in your program
is unable to continue because of some condition outside of the control of the
program (typically I/O), we say that the task or the thread *blocks* (in our
science-fiction story, the clone has knocked on the door and is waiting for it
to open). Without concurrency, the whole program comes to a stop until the
external condition changes. If the program is written using concurrency,
however, the other tasks in the program can continue to execute when one task is
blocked, so the program continues to move forward. In fact, from a performance
standpoint, it makes no sense to use concurrency on a single-processor machine
unless one of the tasks might block.

A common example of performance improvements in single-processor systems is
*event-driven programming*, in particular user-interface programming. Consider
a program that performs some long-running operation and thus ends up ignoring
user input and being unresponsive. If you have a "quit" button, you don't want
to poll it in every piece of code you write. This produces awkward code,
without any guarantee that a programmer won't forget to perform the check.
Without concurrency, the only way to produce a responsive user interface is for
all tasks to periodically check for user input. By creating a separate thread
of execution to respond to user input, the program guarantees a certain level
of responsiveness.

A straightforward way to implement concurrency is at the operating system level,
using *processes*, which are different from threads. A process is a
self-contained program running within its own address space. Processes are
attractive because the operating system usually isolates one process from
another so they cannot interfere with each other, which makes programming with
processes relatively easy. In contrast, threads share resources like memory and
I/O, so a fundamental difficulty in writing multithreaded programs is
coordinating these resources between different thread-driven tasks, so they
cannot be accessed by more than one task at a time.

Some people go so far as to advocate processes as the only reasonable approach
to concurrency,^[Eric Raymond, for example, makes a strong case in *The Art of
UNIX Programming* (Addison-Wesley, 2004).] but unfortunately there are generally
quantity and overhead limitations to processes that prevent their applicability
across the concurrency spectrum. (Eventually you get used to the standard
concurrency refrain, "That approach works in some cases but not in other cases").

Some programming languages are designed to isolate concurrent tasks from each
other. These are generally called *functional languages*, where each function
call produces no side effects (and so cannot interfere with other functions) and
can thus be driven as an independent task. *Erlang* is one such language, and it
includes safe mechanisms for one task to communicate with another. If you find
that a portion of your program must make heavy use of concurrency and you are
running into excessive problems trying to build that portion, you might consider
creating that part of your program in a dedicated concurrency language.

Python took the more traditional approach of adding support for threading on top
of a sequential language.^[It could be argued that trying to bolt concurrency
onto a sequential language is a doomed approach, but you'll have to draw your
own conclusions.] Instead of forking external processes in a multitasking
operating system, threading creates tasks *within* the single process
represented by the executing program.

Concurrency imposes costs, including complexity costs, but can be outweighed by
improvements in program design, resource balancing, and user convenience. In
general, concurrency enables you to create a more loosely coupled design;
otherwise, parts of your code would be forced to pay explicit attention to
operations that would normally be handled by concurrency.

The Four Maxims of Concurrency
------------------------------

After grappling with concurrency over many years, I developed these four
maxims:

> 1. Don't do it
> 2. Nothing is true and everything matters
> 3. Just because it works doesn't mean it's not broken
> 4. You must still understand it

These apply to a number of languages. However, there do exist languages
that are designed to prevent these issues.

### 1. Don't do it

(And don't do it yourself).

The easiest way to avoid entangling yourself in the profound problems produced
by concurrency is not to do it. Although it can be seductive and seem safe
enough to try something simple, the pitfalls are myriad and subtle. If you can
avoid it, your life will be much easier.

The *only* thing that justifies concurrency is speed. If your program isn't
running fast enough---and be careful here, because just *wanting* it to run
faster isn't justification---first apply a profiler (see [Profiling and
Optimizing]) to discover whether there's some other optimization you can
perform.

If you're compelled into concurrency, take the simplest, safest approach to the
problem. Use well-known libraries and write as little of your own code as
possible. With concurrency, there's no such thing as "too simple." Cleverness is
your enemy.

### 2. Nothing is true and everything matters

Programming without concurrency, you've come to expect a certain order and
consistency in your world. With something as simple as setting a variable to a
value, it's obvious it should always work properly.

In concurrency-land, some things might be true and others are not, to the point
where you must assume that nothing is true. You must question everything. Even
setting a variable to a value might or might not work the way you expect, and it
goes downhill from there. I've become familiar with the feeling of discovering
that something I thought should obviously work, actually doesn't.

All kinds of things you can ignore in non-concurrent programming suddenly become
important with concurrency. For example, you must now know about the processor
cache and the problems of keeping the local cache consistent with main memory.
You must understand the deep complexities of object construction so that your
constructor doesn't accidentally expose data to change by other threads. The
list goes on.

Although these topics are too complex to give you expertise in this chapter, you
must be aware of them.

### 3. Just because it works doesn't mean it's not broken

You can easily write a concurrent program that appears to work but is actually
broken, and the problem only reveals itself under the rarest of
conditions---inevitably as a user problem after you've deployed the program.

+   You can't prove a concurrent program is correct, you can only (sometimes)
    prove it is incorrect.

+   Most of the time you can't even do that: If it's broken you probably won't
    be able to detect it.

+   You can't usually write useful tests, so you must rely on code inspection
    combined with deep knowledge of concurrency in order to discover bugs.

+   Even working programs only work under their design parameters. Most
    concurrent programs fail in some way when those design parameters are
    exceeded.

In other areas of programming, we develop a sense of determinism. Everything happens as
promised (or implied) by the language, which is comforting and expected---after
all, the point of a programming language is to get the machine to do what we
want. Moving from the world of deterministic programming into the realm of
concurrent programming, we encounter a cognitive bias called the [Dunning-Kruger
Effect](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect) which can
be summed up as "the less you know, the more you think you know." It means
"...relatively unskilled persons suffer illusory superiority, mistakenly
assessing their ability to be much higher than it really is."

My own experience is that, no matter how certain you are that your code is
thread-safe, it's probably broken. It's all too easy to be very sure you
understand all the issues, then months or years later you discover some concept
that makes you realize that most everything you've written is actually
vulnerable to concurrency bugs. The compiler doesn't tell you when something is
incorrect. To get it right you must hold all the issues of concurrency in your
forebrain as you study your code.

In all the non-concurrent areas of Python, "no obvious bugs and no compiler
complaints" seems to mean that everything is OK. With concurrency, it means
nothing. The very worst thing you can be in this situation is "confident."

### 4. You must still understand it.

After maxims 1-3 you might be properly frightened of concurrency, and think,
"I've avoided it up until now, perhaps I can just continue avoiding it."

This is a rational reaction. You might know about other programming languages
that are better designed to build concurrent programs---even ones that easily
communication with Python). Why not write the concurrent parts in those
languages and use Python for everything else?

Alas, you cannot escape so easily:

+   Even if you never explicitly create a thread, frameworks you use
    might---for example, the Swing Graphical User Interface (GUI) library, or
    something as simple as the `Timer` class.

+   Here's the worst thing: when you create components, you must assume those
    components might be reused in a multithreading environment. Even if your
    solution is to give up and declare that your components are "not
    thread-safe," you must still know enough to realize that such a statement is
    important and what it means.

People sometimes suggest that concurrency is too advanced to include in a book
that introduces the language. They argue that concurrency is a discrete topic
that can be treated independently, and the few cases where it appears in daily
programming (such as graphical user interfaces) can be handled with special
idioms. Why introduce such a complex topic if you can avoid it?

Alas, if only it were so. Unfortunately, you don't get to choose when threads
appear in your programs. Just because you never start a thread
yourself doesn't mean you can avoid writing threaded code. For example, Web
systems are one of the most common applications, and are inherently
multithreaded---Web servers typically contain multiple processors, and
parallelism is an ideal way to utilize these processors. As simple as such a
system might seem, you must understand concurrency to write it properly.

Python is a multithreaded language, and concurrency issues are present whether you
are aware of them or not. As a result, there are many Python programs in use that
either just work by accident, or work most of the time and mysteriously break
every now and again because of undiscovered flaws. Sometimes this breakage is
relatively benign, but sometimes it means the loss of valuable data, and if you
aren't at least aware of concurrency issues, you can end up assuming the problem
is somewhere else rather than in your code. These kinds of issues can also be
exposed or amplified if a program is moved to a multiprocessor system.
Basically, knowing about concurrency makes you aware that apparently correct
programs can exhibit incorrect behavior.

Summary
-------

The only justification for concurrency is "too much waiting." This can also
include the responsiveness of user interfaces, but as Java is effectively not
used to build user interfaces,^[The libraries are there and the language was
intended to be used for this purpose but in practice it happens so rarely as to
be able to say "never."] this simply means "your program isn't running fast
enough."

If concurrency were easy, there would be no reason to avoid it. Because it is
hard, you should consider carefully whether it's worth the effort. Can you
speed things up some other way? For example, move to faster hardware (which can
be a lot less expensive than lost programmer time) or break your program into
pieces and run those pieces on different machines?

Occam's (or Ockham's) razor is an oft-misunderstood principle. I've seen at
least one movie where they define it as "the simplest solution is the correct
one," as if it's some kind of law. It's actually a guideline: When faced with a
number of approaches, first try the one that requires the fewest assumptions.
In the programming world, this has evolved into "try the simplest thing that
could possibly work." When you know something about a particular tool---as you
now know something about concurrency---it can be quite tempting to use it, or
to specify ahead of time that your solution must "run fast," to justify
designing in concurrency from the beginning. But our programming version of
Occam's razor says that you should try the simplest approach first (which will
also be cheaper to develop) and see if it's good enough.

As I came from a low-level background (physics and computer engineering), I was
prone to imagining the cost of all the little wheels turning. I can't count the
number of times I was certain the simplest approach could never be fast enough,
only to discover upon trying that it was more than adequate.

### Drawbacks

The main drawbacks to concurrency are:

1.  Slowdown while threads wait for shared resources.

2.  Additional CPU overhead for thread management.

3.  Unrewarded complexity from poor design decisions.

4.  Pathologies such as starving, racing, deadlock, and livelock (multiple
    threads working individual tasks that the ensemble can't finish).

5.  Inconsistencies across platforms. With some examples, I discovered race
    conditions that quickly appeared on some computers but not
    on others. If you develop a program on the latter, you might get badly
    surprised when you distribute it.

In addition, there's an art to the application of concurrency. Java is designed
to allow you to create as many objects as necessary to solve your problem---at
least in theory.^[Creating millions of objects for finite-element analysis in
engineering, for example, might not be practical in Java without the
*Flyweight* design pattern.] However, `Thread`s are not typical objects: each
has its own execution environment including a stack and other necessary
elements, making it much larger than a normal object. In most environments it's
only possible to create a few thousand `Thread` objects before running out of
memory. You normally only need a handful of threads to solve a problem, so this
is typically not much of a limit, but for some designs it becomes a constraint
that might force you to use an entirely different scheme.

#### The Shared-Memory Pitfall

One of the main difficulties with concurrency occurs because more than one task
might be sharing a resource---such as the memory in an object---and you must
ensure that multiple tasks don't simultaneously read and change that resource.

I have spent years studying and struggling with concurrency. I've learned you
can never believe that a program using shared-memory concurrency is working
correctly. You can discover it's wrong, but you can never prove it's right.
This is one of the well-know maxims of concurrency.^[In science, a theory is
never proved, but to be valid it must be *falsifiable*. With concurrency,
we can't even get falsifiability most of the time.]

I've met numerous people who have an impressive amount of confidence in their
ability to write correct threaded programs. I occasionally start thinking I can
get it right, too. For one particular program, I initially wrote it when we
only had single-CPU machines. I was able to convince myself that, because of
the promises I thought I understood about Java tools, the program was correct.
And it didn't fail on my single-CPU machine.

Fast forward to machines with multiple CPUs. I was surprised when the program
broke, but that's one of the problems. It's not Java's fault; "write once, run
everywhere" cannot possibly extend to concurrency on single vs. multicore
machines. It's a fundamental problem with concurrency. You *can* actually
discover some concurrency problems on a single-CPU machine, but there are other
problems that won't appear until you try it on a multi-CPU machine, where your
threads are actually running in parallel.

As another example, the dining philosophers problem can easily be adjusted so
deadlock rarely happens, giving you the impression that everything is
copacetic.

You can never let yourself become too confident about your programming
abilities when it comes to shared-memory concurrency.
