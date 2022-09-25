import sys
import signal


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(130)


signal.signal(signal.SIGINT, signal_handler)

import os
import readline
from .utils import get_shellrc_file
from .config_file import write_to_config_file
from .const import CONFIG_FILE_PATH, INITIAL_SHELLRC_STRING, INITIATED_SHELLRC_STRING


def check_for_initiation():
    if os.path.exists(CONFIG_FILE_PATH):
        return

    try:
        default_editor = input('Your Default Editor (leave blank to use code): ')
    except EOFError:
        sys.exit(1)

    paths = []
    while True:
        try:
            path = input("Enter a path to search for projects (leave blank if you are done): ")
        except EOFError:
            sys.exit(1)
        if path == '':
            if paths == []:
                print("You have to enter at least one path.")
                continue
            break
        if os.path.isdir(path):
            paths.append(os.path.abspath(path))
        else:
            print(f"'{path}' is not a directory.")

    config_file = {
        "paths": paths,
        "default_editor": default_editor if default_editor != '' else 'code'
    }

    write_to_config_file(config_file)

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
    from .cli import cli # It has to be here or it will raise an error
    cli()
