def count(a, b):
  while True:
    yield a # any function that contains a yield statement returns a generator, generator and iterators are interchangeable
    a += b
x = count(10,2)
print(next(x))
print(next(x))
print(next(x))

from types import FunctionType, MethodType, LambdaType, GeneratorType, ModuleType
from _collections_abc import Iterable, Collection, Sequence
x = isinstance([1,2,3], Iterable)
print(x)
from numbers import Complex, Real, Rational, Integral, Number
isinstance(123, Number)
from statistics import mean, median, variance, stdev, quantiles
from random import choice

x = 9.0
x.isdecimal()
x.isdigit()
x.isnumeric()
x.isalnum()
x.isprintable()
x.isspace()

from functools import reduce, partial, wraps, lru_cache, total_ordering #decorator
from collections import namedtuple, abc, deque, defaultdict
from enum import Enum, auto
from dataclasses import make_dataclass,field, dataclass
from copy import copy, deepcopy
import sys
file = sys.stderr
arg = sys.argv[0]
import pprint
import sqlite3
import threading
import asyncio
import curses
from time import perf_counter #profiling
from timeit import timeit,Timer
import wave #audio
from struct import pack
import array