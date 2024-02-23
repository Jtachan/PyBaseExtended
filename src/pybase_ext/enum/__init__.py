"""
Different enumerations types supported for python >= 3.8
"""
__all__ = ["StrEnum", "TupleEnum", "auto", "IntEnum", "IntFlag", "Flag", "unique"]
from enum import Flag, IntEnum, IntFlag, auto, unique

from ._types import StrEnum, TupleEnum
