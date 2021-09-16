from dataclasses import dataclass


@dataclass
class ObsVariable:
    new_name: str
    prev_name: str
