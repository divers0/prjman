import os
from .const import DEFAULT_EDITOR_FILE_PATH


def find_all_projects():

    projects = []

    for prj_category in ('gitclones', 'OnGit', 'NotOnGit'):
        for prj in [os.path.join("/home/diverso/p", prj_category, x) for x in os.listdir(os.path.join("/home/diverso/p", prj_category)) if os.path.isdir(os.path.join("/home/diverso/p", prj_category, x))]:
            projects.append(Project(prj.split("/")[-1], prj))

    return projects


def get_default_editor():
    with open(DEFAULT_EDITOR_FILE_PATH, 'r') as f:
        s = f.read().strip()
    return s


def set_default_editor(new_editor):
    with open(DEFAULT_EDITOR_FILE_PATH, 'w') as f:
        f.write(new_editor)


class Project(object):
    def __init__(self, name: str, path: str):
        self.NAME = name
        self._path = path

    def __repr__(self) -> str:
        return f"Project(name={self.name}, path={self.path})"

    @property
    def name(self):
        return self.NAME

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
