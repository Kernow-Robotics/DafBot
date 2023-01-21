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


def generate_random_daffodil(spawn_volume: GantryWorkspace) -> Daffodil:
    """
    Randomly places a Daffodil object with randomized attributes
    within the specified spawn volume.
    """
    x = randint(
        spawn_volume.x_min,
        spawn_volume.x_max,
    )
    y = randint(
        spawn_volume.y_min,
        spawn_volume.y_max,
    )
    z = randint(
        spawn_volume.z_min,
        spawn_volume.z_max,
    )

    coord = Target(x, y, z)

    return Daffodil(location=coord, mature=choice([True, False]))


def generate_list_of_random_daffodils(
    spawn_volume: GantryWorkspace,
    list_length: int = 1,
) -> list[Daffodil]:
    """
    Gimmie many pretty daffodils!
    """
    return [generate_random_daffodil(spawn_volume) for i in range(list_length)]
