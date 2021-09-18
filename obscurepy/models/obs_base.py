from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class ObsBase(ABC):
    """Abstract base class for Obs model objects

    Attributes:
        **new_name (str)**: New obscured name

        **prev_name (str)**: Previous unobscured name
    """
    new_name: str
    prev_name: str

    def __new__(cls, *args, **kwargs):
        """Prevents this base class from being instantiated"""
        if cls == ObsBase:
            raise TypeError('ObsBase is an abstract class!')
        return super().__new__(cls)

    @abstractmethod
    def __hash__(self):
        pass
