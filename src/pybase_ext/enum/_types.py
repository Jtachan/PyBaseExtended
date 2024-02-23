"""
New enum types supported for python >= 3.7
"""
import builtins
import enum


class StrEnum(builtins.str, enum.Enum):
    """Enumeration where members are strings."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values) -> str:
        """
        Generates the default value as the name of the member in lower case when
        'auto()' is called. For example, member 'RED = auto()' generates 'red' as
        its value.
        """
        return name.lower()


class TupleEnum(builtins.tuple, enum.Enum):
    """Enumeration where members are tuples."""
