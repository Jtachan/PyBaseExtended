"""
New enum types supported for python >= 3.7
"""
import builtins
import enum


class ReprEnum(enum.Enum):
    """Changes the repr() and str(), leaving format() to the mixed-in type."""
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class StrEnum(builtins.str, ReprEnum):
    """Enumeration where members are strings."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values) -> str:
        """
        Generates the default value as the name of the member in lower case when
        'auto()' is called. For example, member 'RED = auto()' generates 'red' as
        its value.
        """
        return name.lower()


class TupleEnum(builtins.tuple, ReprEnum):
    """Enumeration where members are tuples."""
