from dataclasses import dataclass


@dataclass
class ObsFunction:
    new_name: str
    prev_name: str
    variables: set
    functions: set
    args: set
    return_val: str
