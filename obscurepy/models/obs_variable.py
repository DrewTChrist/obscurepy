from dataclasses import dataclass
from obscurepy.models.obs_base import ObsBase


@dataclass
class ObsVariable(ObsBase):
    """Object to maintain data for python variables that have been visited"""

    def __hash__(self):
        """Hashes by new name and previous name"""
        return hash((self.new_name, self.prev_name))
