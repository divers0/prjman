import sys
import signal


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(130)


signal.signal(signal.SIGINT, signal_handler)

import os
from .utils import get_shellrc_file
from .const import CONFIG_FOLDER_PATH
from .projects import set_default_editor


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


initial_shellrc_string = f"""\n
prjman() {{
    projman
}}
"""

def check_for_command_in_shellrc():
    new_shellrc_string = f"""\n
prjman() {{
    eval $(projman "$@")
}}
"""
    shellrc_file_path, shellrc_file = get_shellrc_file()
    if new_shellrc_string not in shellrc_file:
        if initial_shellrc_string in shellrc_file:
            shellrc_file = shellrc_file.replace(initial_shellrc_string, new_shellrc_string)
        else:
            shellrc_file += new_shellrc_string
        with open(shellrc_file_path, 'w') as f:
            f.write(shellrc_file)


def main():
    check_for_command_in_shellrc()
    check_for_initiation()
    from .cli import cli # It has to be here
    cli()
