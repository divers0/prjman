import os
from .config_file import read_config_file, write_to_config_file


def find_all_projects(path, ignore):
    ignores = ['node_modules', '.venv', 'venv', 'env', '.env', '.idea']+ignore
    projects_paths = _scan_for_projects(path, ignores)
    projects = []
    for prj in projects_paths:
        projects.append((prj.split('/')[-1], prj))
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
    return read_config_file()['default_editor']


def set_default_editor(new_editor):
    config_file = read_config_file()
    config_file['default_editor'] = new_editor
    write_to_config_file(new_editor)
