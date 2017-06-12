General
=======

Concurrency: Taking a program that isn't running fast enough, breaking it into
pieces, and "running those pieces separately." The what and how of "running separately"
is where all the details and complexity lie for the various concurrency strategies.

- Idea: Usually the driver is "not fast enough" but sometimes (ironically) it can be
  "too complicated." Some concurrency solutions simplify the problem enough to make
  them attractive for other than speed reasons!

The concept of whether something is synchronous refers to when a function
finishes vs. when a function returns. In the vast majority of Python code these
two points are identical, a.k.a synchronous: a function returns when it
finishes. But with an asynchronous call, the function returns control to the
caller *before* the function finishes---typically much sooner. So the two
events, returning and finishing, now happen at different points in time: they
are *asynchronous*.

If tasks don’t wait on each other then they are compute intensive

Ideally, make tasks that don’t block on other tasks (deadlock prone)


## For Study and Exploration
> Feel free to pull-request something you think might be helpful here

- Concurrency Overviews
  - [Ted Leung](http://www.slideshare.net/twleung/a-survey-of-concurrency-constructs)
  - [The Art of Multiprocessor Programming, Revised Reprint](http://amzn.to/2j1oneL)

- Actors:
  - [Thespian Docs](http://godaddy.github.io/Thespian/doc/)
  - [Thespian Motivation](https://engineering.godaddy.com/why-godaddy-built-an-actor-system-library/)
  - Can Ponylang interface with Python?

- Async:
  - [Christian Medina](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32#.l8tws7nkv)
  - [PyMotw overview](https://pymotw.com/3/asyncio/index.html)
  - [Web Crawler, Guido et. al.](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)
  - [Mike Bayer on Async](http://techspot.zzzeek.org/2015/02/15/asynchronous-python-and-databases/)

- Communicating Sequential Processes (CSP)
  - [PyCSP](https://github.com/runefriborg/pycsp/wiki)
  - [PyCSP Slides](http://arild.github.io/csp-presentation/#1)

- [Join Calculus](https://en.wikipedia.org/wiki/Join-calculus)
  - [Chymyst — declarative concurrency in Scala](https://github.com/Chymyst/chymyst-core/) -- good resource for
    ideas and examples.
  - [Join-calculus for Python](https://github.com/maandree/join-python)

- AioHTTP:
  - [Docs](http://aiohttp.readthedocs.io/en/stable/)
  - [An Intro](http://stackabuse.com/python-async-await-tutorial/)

- Curio
  - [Difference between asyncio and curio](https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/)
  - [Docs](http://curio.readthedocs.io/en/latest/)
  - [Repo](https://github.com/dabeaz/curio)
  
- Remote Objects
  - [Pyro4](https://pythonhosted.org/Pyro4/) Mature Python remote object implementation.

- Calling Go from Python (example of taking advantage of another language's concurrency model)
  - [Example](https://github.com/jbuberel/buildmodeshared/tree/master/gofrompython)
    (For windows it would have to be done in the bash shell but that might be OK)
  - RabbitMQ allows cross-language calls.

- An example: Each task controls a pixel/block on the screen. Produces a visual,
  graphic idea of what's going on.
  - Which graphics library to use?
  - [Processing](http://py.processing.org/)
  - [Tkinter](http://stackoverflow.com/questions/4842156/manipulating-individual-pixel-colors-in-the-tkinter-canvas-widget)

- Asyncio example: Webcomic Reader
  - Text-file database keeps track of last comic read
  - Each comic is simply opened in a browser tab

- [Pachyderm Pipeline System](http://docs.pachyderm.io/en/latest/reference/pachyderm_pipeline_system.html)
  - [Slack channel]( http://slack.pachyderm.io/)
  - "Our official release for the CLI are for OSX and Linux as of now.  However, we do have windows users that work with Pachyderm via the new Linux subsystem in Windows 10.  Also, the CLI is only one choice for interacting with Pachyderm.  You can also use the Python, Go, or other client, which should work just fine on Windows."

- Misc
  - Bridge between Python and Java: https://www.py4j.org/

What Confuses You About Concurrency?
====================================
(Notes from an open-spaces session at Pycon 2017)

- I don't want to think about it.
- What about testing? New different kinds of failure modes introduced by concurrency.
- Making sure an event is handled.
- Martin Fowler's recent Youtube presentation on event-driven programming.
- Twelve-factor application (Heroku came up with this term and has the list) to make things easily scalable
- How to write things that can easily be scaled without being a hassle
- Does async and await preclude gevent, twisted, etc.
- How do I write code/libraries compliant with async and await?

Tools
=====

- Pipenv
- Codeclimate


Miscellaneous
=============

> Many of these were collected for a general Python book, not necessarily for concurrency

- Code style checkers: flake8 and hacking

- ptpython: better python REPL

- logging instead of print()

- tabulate and texttable for generating text tables.

- Peewee ORM as database example, data storage

- Debuggers:
    PuDB
    WDB web debugger

- Testing:
    Behave, Gherkin, assertpy, hypothesis, robotframework
    https://testrun.org/tox/latest/

- matplotlib

- tqdm progress bar

- Simple object serialization: http://marshmallow.readthedocs.org/en/latest/

- Auto-reformatters:
    https://github.com/google/yapf

- List example:
  things_i_love = ["meaningful examples", "irony", "lists"]

- "Fight with the problem, not with the language"

- http://www.pythontutor.com/

- Python 3 special but basic features:
https://asmeurer.github.io/python3-presentation/slides.html

- PUDB debugger (screen text based)

- Formatting: https://pypi.python.org/pypi/autopep8/

- Design by contract: http://andreacensi.github.io/contracts/

- dbm for databases ("Storing data")

- Interacting with C? (cffi)

- Requests library for HTTP http://docs.python-requests.org/en/latest/

- https://testrun.org/tox/latest/

- Beck Design Rules: http://martinfowler.com/bliki/BeckDesignRules.html

- Bound Inner Classes: http://code.activestate.com/recipes/577070-bound-inner-classes/

- Message broker:
    http://www.rabbitmq.com/tutorials/tutorial-one-python.html

- Download, install, configure:
    https://github.com/princebot/pythonize

- Functional programming:
    http://toolz.readthedocs.org/en/latest/api.html

- Things that should be builtins?
    https://boltons.readthedocs.org/en/latest/

- Best Python Quotes (for text examples):
    http://www.telegraph.co.uk/comedy/comedians/monty-python-s-25-funniest-quotes/life-of-brian-tedious-prophet/

- Single interface to environment variables’, configuration files’, and command line arguments’ provided values:
    https://pypi.python.org/pypi/crumbs

- "Hidden" features:
    http://stackoverflow.com/questions/101268/hidden-features-of-python
