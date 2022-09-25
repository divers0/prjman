import os
from .const import DEFAULT_EDITOR_FILE_PATH


def find_all_projects(path, ignore):
    ignores = ['node_modules', '.venv', 'venv', 'env', '.env', '.idea']+ignore
    projects_paths = _scan_for_projects(path, ignores)
    projects = []
    for prj in projects_paths:
        projects.append(Project(prj.split('/')[-1], prj))
    return projects


def _scan_for_projects(path, ignore, paths=[]):
    contents = [os.path.join(path, x) for x in os.listdir(path)]
    for content in contents:
        if os.path.isdir(content) and content.split('/')[-1] not in ignore:
            if any(1 for x in os.listdir(content) if x in ['.git', '.gitignore', 'READNE.md', 'setup.py', 'Makefile', 'CMakeLists.txt', 'LICENSE', 'docs']):
                paths.append(content)
            else:
                _scan_for_projects(content, ignore, paths)
    return paths


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
