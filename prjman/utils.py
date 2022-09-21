from .const import ANSI_COLOR_NAMES


def colorize(s, color):
    return "\033[3" + str(ANSI_COLOR_NAMES.get(color)) + f"m{s}\033[0m"
