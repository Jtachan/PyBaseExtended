"""Test the 'enums' module."""
from pybase_ext import enum


def test_repr_enum():
    """
    Testing behaviors in existing enums that were modified in newer python releases,
    due to the creation of ReprEnum.
    The used classes are obtained from the documentation examples.
    """

    class Color(enum.IntFlag):
        RED = enum.auto()
        GREEN = enum.auto()

    assert Color.RED & 2 is Color(0)
    assert repr(Color.RED | 2) == "<Color.RED|GREEN: 3>"
    assert str(Color.RED) == "1"

    class Number(enum.IntEnum):
        ONE = 1
        TWO = enum.auto()
        THREE = 3

    assert Number.TWO == 2
    assert Number.ONE + Number.THREE == 4
    assert repr(Number.ONE) == "<Number.ONE: 1>"
    assert str(Number.TWO) == "2"


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
