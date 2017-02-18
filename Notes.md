
- Actors:
  - http://godaddy.github.io/Thespian/doc/
  - https://engineering.godaddy.com/why-godaddy-built-an-actor-system-library/

- Async:
  - http://stackabuse.com/python-async-await-tutorial/
  - https://pymotw.com/3/_sources/asyncio/index.txt
  - http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
  - https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/
  - http://techspot.zzzeek.org/2015/02/15/asynchronous-python-and-databases/

- Curio
  - http://curio.readthedocs.io/en/latest/
  - https://github.com/dabeaz/curio


http://www.slideshare.net/twleung/a-survey-of-concurrency-constructs


The Art of Multiprocessor Programming, Revised Reprint
http://amzn.to/2j1oneL


Calling Go from Python:
https://github.com/jbuberel/buildmodeshared/tree/master/gofrompython
For windows it would have to be done in the bash shell but that might be OK

RabbitMQ allows cross-language calls.

If tasks don’t wait on each other then they are compute intensive

Ideally, make tasks that don’t block on other tasks (deadlock prone)

The concept of whether something is synchronous refers to when a function
finishes vs. when a function returns. In the vast majority of Python code these
two points are identical, a.k.a synchronous: a function returns when it
finishes. But with an asynchronous call, the function returns control to the
caller *before* the function finishes---typically much sooner. So the two
events, returning and finishing, now happen at different points in time: they
are *asynchronous*.

Demo: each coroutine controls a pixel
http://stackoverflow.com/questions/4842156/manipulating-individual-pixel-colors-in-the-tkinter-canvas-widget

Miscellaneous
=============

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
