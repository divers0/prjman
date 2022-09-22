import pyperclip as pc
from .const import ANSI_COLOR_NAMES


def colorize(s, color):
    return "\033[3" + str(ANSI_COLOR_NAMES.get(color)) + f"m{s}\033[0m"


def copy_to_clipboard(text):
    pc.copy(text)
