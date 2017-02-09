Preface
=======

> This is an intermediate-to-advanced book on concurrency in Python.

The reader is assumed to already be fluent in the Python language. There are a
large number and variety of resources available to achieve this fluency, many of
them free.

In addition, I use the latest version of Python available at this writing,
version 3.6, which includes important concurrency features. If you are wedded to
an earlier version of Python, this book might not be for you.

That said, this book *is* an introduction to the concepts and applications of
concurrency in Python, for a beginner *to those topics*. I start from scratch,
assuming you've never heard the term before or any of the surrounding ideas.
This is a very reasonable approach because concurrency is relatively orthogonal
to the rest of programming and it's entirely possible to be an expert in
everything about a language for years before exploring concurrency for the first
time.

A Strange but Pragmatic Approach
--------------------------------

Virtually every discussion of concurrency starts with the complex, low-level
nuts and bolts and then slowly works up to the more elegant high-level
solutions. This is understandable because it's how we teach everything else.

Concurrency is a strange topic in just about every conceivable way. As you shall
learn in this book, the *only* justification for wading into the complexity and
tribulations of concurrency is to make your program run faster. And if that's
truly what you need, you probably *don't* need to learn everything about
concurrency. What you'd really like is the shortest, easiest path to a faster
program.

So that's how I organize the book. After explaining what concurrency is, we'll
start with the simplest and easiest---and typically, the highest
level---approaches to speeding up your program with concurrency. As the book
progresses, the techniques will become lower-level, messier, and more
complicated. The goal is that you'll go only as far as you need in order to
solve your speed problem, and after that you'll only go further if you're
interested, or when you come back later with a new problem.

eBook First
-----------

This book is developed in the open, as an eBook. Although I haven't yet settled
on a license, my intent is for the eBook to remain free.

At the 2016 Pycon in Portland, I held an open-spaces session around this book,
and also attended a dinner where we talked about it. In both cases people argued
that, while they really liked the idea of a free eBook, eventually they want a
print book. Once the eBook version has been out long enough to evolve and settle
down, and also to get adequate feedback to eliminate errors, I will revisit the
issue and consider creating a print version of the book.

Business Model
--------------

My two most recent books, [Atomic Scala](www.AtomicScala.com) and [On Java
8](www.OnJava8.com), were not free. In the process of developing those books I
became aware that a big part of that choice was that---while I enjoyed learning
about those languages and writing those books---I ultimately didn't want to do
further work in those areas, so there was no additional financial support
(seminars, consulting, etc.) created from those books. They needed to be their
own endpoints.

The Python community has called to me ever since I discovered it. I have
postponed that call for a couple of decades, with the excuse "let me just finish
this one thing, then I'll come join you" (an all-too-familiar refrain heard by
the partners of computer programmers). I evolve slowly, but I know now that the
Python community is where I'm happiest.

While the thought of struggling with the arbitrary limitations and roadblocks
of, say, the Java language (for details, see [On Java 8](www.OnJava8.com)) in a
training or consulting context fills me with angst, the vision of working with
people who already know the productivity and delights of Python fills me with
joy. That's where I want to live, and I want this book to lay the groundwork for
conferences, developer retreats, consulting, training, and other experiences. I
believe it will satisfy my need for fun and fulfillment.

I could certainly have taken the approach I've used in my other books and
created an introductory Python book, but there are a vast number of those which
do an outstanding job. I don't see myself making a big contribution there.
Instead, I chose something I think most folks experience as quite challenging.
Over the decades, I have had periodic, intense bouts with concurrency. I've come
away from each of these believing that, finally, I understand the topic. And
each time I've discovered later there was some gaping hole in my knowledge. You
will discover that concurrency consistently produces excellent examples of the
[Dunning-Kruger
Effect](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect), where the
less you know, the more you think you know. I know enough about concurrency to
know there can *always* appear some surprising hole in my knowlege.

Source Code
-----------

All the source code for this book is available as copyrighted freeware,
distributed along with the sources for the book's text, via
[Github](https://github.com/BruceEckel/ConcurrentPython). To make sure you get
the most current version, this is the official code distribution site.

Coding Standards
----------------

In the text of this book, identifiers (keywords, methods, variables, and class
names) are set in bold, fixed-width `code font`. Some keywords, such as `class`,
are used so much that the bolding can become tedious. Those which are
distinctive enough are left in normal font.

The code files in this book are tested with an automated system, and should work
without compiler errors (except those specifically tagged) in the latest version
of Python.

Bug Reports
-----------

No matter how many tools a writer uses to detect errors, some always creep in
and these often leap off the page for a fresh reader. If you discover anything
you believe to be an error, please submit the error along with your suggested
correction, for either the book's prose or examples,
[here](https://github.com/BruceEckel/ConcurrentPython/issues). Your help is
appreciated.

Mailing List
------------

For news and notifications, you can subscribe to the low-volume email list at
[www.ConcurrentPython.com](http://www.ConcurrentPython.com). I don't use ads and
strive to make the content as appropriate as possible.

Colophon
--------

This book was written with Pandoc-flavored Markdown, and produced into ePub
version 3 format using [Pandoc](http://pandoc.org/).

The body font is Georgia and the headline font is Verdana. The code font is
Ubuntu Mono, because it is especially compact and allows more characters on a
line without wrapping. I chose to place the code inline (rather than make
listings into images, as I've seen some books do) because it is important to me
that the reader be able to resize the font of the code listings when they resize
the body font (otherwise, really, what's the point?).

The build process for the book is automated, as well as the process to extract,
compile and test the code examples. All automation is achieved through fairly
extensive programs I wrote in Python 3.

### Cover Design


Thanks
------


Dedication
----------

