from setuptools import setup, find_packages
from prjman.utils import get_shellrc_file, change_items_index
from prjman.const import INITIAL_SHELLRC_STRING, INITIATED_SHELLRC_STRING


VERSION = "0.2.5"


def check_for_command_in_shellrc():
    shellrc_file_path, shellrc_file = get_shellrc_file()
    sign_of_prjman_alias = ("alias prjman=", "alias projman=")

    if INITIAL_SHELLRC_STRING not in shellrc_file and INITIATED_SHELLRC_STRING not in shellrc_file:
        shellrc_file += INITIAL_SHELLRC_STRING
        if any(1 for x in shellrc_file.split('\n') if x.startswith(sign_of_prjman_alias)):
            shellrc_file_lines = shellrc_file.split('\n')
            change_items_index(shellrc_file_lines, [x for x in shellrc_file_lines if x.startswith(sign_of_prjman_alias)][0], len(shellrc_file_lines))
            shellrc_file = '\n'.join(shellrc_file_lines)
        with open(shellrc_file_path, 'w') as f:
            f.write(shellrc_file)


setup(
    name='prjman',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'projman = prjman:main',
        ],
    },
)


check_for_command_in_shellrc()
