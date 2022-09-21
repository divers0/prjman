import sys
import signal


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(130)


signal.signal(signal.SIGINT, signal_handler)
import os
import pickle
from .const import *


def check_for_initiation():
    if os.path.exists(CONFIG_FOLDER_PATH):
        return
    from .projects import set_default_editor
    os.mkdir(CONFIG_FOLDER_PATH)
    with open(PROJECTS_FILE_PATH, "wb") as f:
        pickle.dump([], f)
    default_editor = input('Your Default Editor (press enter to use code): ')
    set_default_editor(default_editor if default_editor != '' else 'code')
    print('Done.')
    sys.exit()


class Project(object):
    def __init__(self, name: str, path: str, project_category: str):
        self.NAME = name
        self._path = path
        self._project_category = project_category

    def __repr__(self) -> str:
        return f"Project(name={self.name}, path={self.path}, project_category={self.project_category})"

    @property
    def name(self):
        return self.NAME

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def project_category(self):
        return self._project_category

    @project_category.setter
    def project_category(self, project_category):
        self._project_category = project_category


def main():
    check_for_initiation()
    from .cli import cli
    cli()

