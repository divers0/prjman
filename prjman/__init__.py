import sys
import signal


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(130)


signal.signal(signal.SIGINT, signal_handler)
import os
from .const import CONFIG_FOLDER_PATH
from .projects import set_default_editor


def check_for_initiation():
    if os.path.exists(CONFIG_FOLDER_PATH):
        return

    os.mkdir(CONFIG_FOLDER_PATH)

    default_editor = input('Your Default Editor (press enter to use code): ')
    set_default_editor(default_editor if default_editor != '' else 'code')

    print('Done.')
    sys.exit()


def main():
    check_for_initiation()
    from .cli import cli # It has to be here
    cli()
