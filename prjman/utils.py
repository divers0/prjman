import os

from .const import ANSI_COLOR_NAMES


def colorize(s, color):
    return "\033[3" + str(ANSI_COLOR_NAMES.get(color)) + f"m{s}\033[0m"


def get_shellrc_file():
    shell = os.getenv("SHELL").split("/")[-1]
    shellrc_file_path = os.path.expanduser(f"~/.{shell}rc")
    with open(shellrc_file_path, "r") as f:
        shellrc_file = f.read()
    return shellrc_file_path, shellrc_file


def change_items_index(l, item, new_index):
    l.remove(item)
    l.insert(new_index, item)


def validate_multi_value_options(option_value):
    return [x for x in ",".join(option_value).split(",") if x != ""]
