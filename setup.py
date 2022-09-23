from prjman.utils import get_shellrc_file
from prjman import initial_shellrc_string
from setuptools import setup, find_packages


VERSION = "0.2.0"


def check_for_command_in_shellrc():
    shellrc_file_path, shellrc_file = get_shellrc_file()

    if initial_shellrc_string not in shellrc_file:
        shellrc_file += initial_shellrc_string
        with open(shellrc_file_path, 'w') as f:
            f.write(shellrc_file)
        print(f"Please enter 'source {'~/'+shellrc_file_path.split('/')[-1]}'"
              " or restart your shell to use the command.")


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
