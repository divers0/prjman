import sys
import signal


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(130)


signal.signal(signal.SIGINT, signal_handler)

import os
from .utils import get_shellrc_file
from .projects import set_default_editor
from .const import CONFIG_FOLDER_PATH, INITIAL_SHELLRC_STRING, INITIATED_SHELLRC_STRING


def check_for_initiation():
    if os.path.exists(CONFIG_FOLDER_PATH):
        return

    os.mkdir(CONFIG_FOLDER_PATH)

    default_editor = input('Your Default Editor (press enter to use code): ')
    set_default_editor(default_editor if default_editor != '' else 'code')


    shellrc_file_path, _ = get_shellrc_file()
    print(f"Please enter 'source {'~/'+shellrc_file_path.split('/')[-1]}'"
          " or restart your shell to use the command.")
    print('Done.')
    sys.exit()


def check_for_command_in_shellrc():
    shellrc_file_path, shellrc_file = get_shellrc_file()
    if INITIATED_SHELLRC_STRING not in shellrc_file:
        if INITIAL_SHELLRC_STRING in shellrc_file:
            shellrc_file = shellrc_file.replace(INITIAL_SHELLRC_STRING, INITIATED_SHELLRC_STRING)
        else:
            shellrc_file += INITIATED_SHELLRC_STRING
        with open(shellrc_file_path, 'w') as f:
            f.write(shellrc_file)


def main():
    check_for_command_in_shellrc()
    check_for_initiation()
    from .cli import cli # It has to be here
    cli()
