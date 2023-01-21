from dataclasses import dataclass
from random import randint, choice


@dataclass(frozen=True)
class GantryWorkspace:
    """
    The gantry's permissible operating volume.
    Cannot be changed after instantiation (immutable).
    """
    x_min: int = 0
    x_max: int = 730
    y_min: int = 0
    y_max: int = 220
    z_min: int = -235
    z_max: int = 0
    home_coord: tuple[int, int, int] = (730, 0, 0)


@dataclass
class Target:
    """
    Defines a point in space representing some target.
    """
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class Daffodil:
    """
    Holds some actionable information about a target daffodil.
    Values cannot be changed after instantiation (immutable).
    """
    location: Target
    mature: bool
