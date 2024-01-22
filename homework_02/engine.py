"""
create dataclass `Engine`
"""
import dataclasses


@dataclasses.dataclass
class Engine(object):
    volume: int
    pistons: int
