from gantry import Gantry
from gantry import FindCOMPort as FCOM
from daffodil import Target, Daffodil, GantryWorkspace, generate_list_of_random_daffodils
import click


def picking_cycle(dafBot: Gantry, daffodil: Daffodil, workspace: GantryWorkspace) -> None:
    """
    Use the gripper to pick the input Daffodil object and place it in a
    basket that is located at the Gantry's home position.
    The lowest possible gantry reach is used to specify both the picking depth
    and how far the gripper moves into the basket when releasing the daffodil.
    """

    # Specifying some waypoints
    above_daffodil = daffodil.location
    above_basket = workspace.home_coord
    enveloping_daffodil = \
        Target(
            daffodil.location.x,
            daffodil.location.y,
            daffodil.location.z - abs(workspace.z_min),
        )
    inside_basket = \
        Target(
            workspace.home_coord.x,
            workspace.home_coord.y,
            workspace.home_coord.z - abs(workspace.z_min),
        )

    # Executing picking cycle
    dafBot.move(above_daffodil, 11000)
    dafBot.gripper_open()
    dafBot.move(enveloping_daffodil, 11000)
    dafBot.gripper_close()
    dafBot.move(above_daffodil, 11000)
    dafBot.move(above_basket, 11000)
    dafBot.move(inside_basket, 11000)
    dafbot.gripper_open()
    dafBot.move(above_basket, 11000)


def generate_gantry_with_lim_switches() -> Gantry:
    dafBot = Gantry(FCOM())
    dafBot.home_all()
    return dafBot


def generate_gantry_without_lim_switches() -> Gantry:
    dafBot = Gantry(FCOM())
    # Assigns current position as 0,0,0, make sure you move head to start position to ensure it sets home correctly.
    dafBot.send_command('$X')
    dafBot.move([0, 0, 240], 11000)
    dafBot.set_current_position_as_home()
    return dafBot


@click.command()
@click.option(
    '--no-lim-switches',
    is_flag=True,
    show_default=True,
    default=False,
    help='Specify that the gantry is NOT using limit switches.'
)
def demo(**kwargs: dict[str, str]) -> None:
    """
    Generates a list of random virtual daffodils and proceeds to pick them
    if the Daffodil is classified as mature.
    This is a basic movement pattern for demonstrating the gantry and gripper.
    """
    print(kwargs)
    dafBot = generate_gantry_without_lim_switches() if kwargs.get("no_lim_switches") else generate_gantry_with_lim_switches()
    a_field_of_flowers = \
        generate_list_of_random_daffodils(
            spawn_volume=GantryWorkspace(),
            list_length=100,
        )
    note = ""
    for daffodil in a_field_of_flowers:
        if daffodil.is_mature:
            picking_cycle(
                dafBot=dafBot,
                daffodil=daffodil,
                workspace=GantryWorkspace()
            )
        else:
            note = " NOT "
        print(f"The following daffodil was classified as{note}mature and has{note}been picked:")
        print(f"{daffodil}\n")


if __name__ == "__main__":
    demo()
