# PyBase-Ext: Enumerations

`pybase-ext` allows using the `enum` module just as the original, with the only difference at the import.

```python
from pybase_ext import enum

class Number(enum.IntEnum):
    """Enumeration using the original 'IntEnum' call"""
    ONE = enum.auto()
    TWO = 2

class Animal(enum.StrEnum):
    """Supported original 'StrEnum' for python versions < 3.11"""
    CAT = enum.auto()
    DOG = "dog"

class Color(enum.TupleEnum):
    """Experimental 'TupleEnum' class"""
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
```

## Index

- [Backported](#backported-classes)
  - [StrEnum](#strenum)
- [Experimental]
  - [TupleEnum]

## Backported classes

### [**StrEnum**](https://docs.python.org/3.11/library/enum.html#enum.StrEnum)

_StrEnum_ is the same as _Enum_, but its members are also strings and can be used in most of the same places that a string can be used.
Backported from Py-3.11.

```pycon
>>> from pybase_ext import enum
>>> class Animal(enum.StrEnum):
...    CAT = enum.auto()
...    DOG = "dog"
...
>>> Animal.CAT
cat
>>> Animal.DOG.title()
'Dog'
>>> Animal.CAT == "cat"
True
>>> Animal.CAT + Animal.DOG
'catdog'
>>> " and ".join(list(Animals))
'cat and dog'
```

**Note**: Using [`auto`](https://docs.python.org/3.12/library/enum.html#enum.auto) results in the lower-cased member name as the value.

## Experimental classes

### **TupleEnum**

_TupleEnum_ is the same as _Enum_, but its members are also tuples and can be used anywhere as tuples can be used.

```pycon
>>> from pybase_ext import enum
>>> class Color(enum.TupleEnum):
...    """Experimental 'TupleEnum' class"""
...    BLACK = (0, 0, 0)
...    WHITE = (255, 255, 255)
...
>>> Color.BLACK
(0, 0, 0)
>>> list(Color.WHITE)
[255, 255, 255]
```

**Note**: Using [`auto`](https://docs.python.org/3.12/library/enum.html#enum.auto) is not supported by _TupleEnum_, and it will raise a `.
