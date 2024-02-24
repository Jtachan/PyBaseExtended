# Python Base Extension

`pybase-ext` allows using its modules just as the original ones, with the only difference at the import.

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
- **All modules**
  - [`enum`](enum.md)
- **Backported modules**
  - [`enum`](enum.md#backported-classes)
- **Experimental classes**
  - [`enum`](enum.md#experimental-classes)