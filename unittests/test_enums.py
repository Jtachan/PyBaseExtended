"""Test the 'enums' module."""
from pybase_ext import enum


def test_str_enum():
    """Testing pybase_ext.enum.StrEnum"""

    class Animals(enum.StrEnum):
        DOG = enum.auto()
        CAT = "cat"
        PLATYPUS = enum.auto()

    for pet in Animals:
        assert isinstance(pet, str), "Type not defined correctly"
        assert pet.upper() == str(pet.value).upper(), "str functions are not working"

    assert list(Animals) == [
        "dog",
        "cat",
        "platypus",
    ], "Formatting not working"


def test_tuple_enum():
    """Testing pybase_ext.enum.TupleEnum"""

    class Colors(enum.TupleEnum):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

    for c in Colors:
        assert isinstance(c, tuple), "Type not defined correctly"
        assert c[0] in c, "tuple functions are not working"

    assert list(Colors) == [(255, 255, 255), (0, 0, 0)], "Formatting not working"
