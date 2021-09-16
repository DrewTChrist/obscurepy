from dataclasses import dataclass


@dataclass
class ObsClass:
    new_name: str
    prev_name: str
    variables: set
    properties: set
    methods: set
    bases: set
