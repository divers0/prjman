import os
from . import Project
from .const import DEFAULT_EDITOR_FILE_PATH


def find_all_projects():

    projects = []

    projects_categorized = {x: [os.path.join(x, y) for y in os.listdir(x) if os.path.isdir(os.path.join(x, y))] for x in [os.path.join('/home/diverso/p/', i) for i in ('gitclones', 'OnGit', 'NotOnGit')]}

    for prj_category in projects_categorized:
        for p in projects_categorized[prj_category]:
            projects.append(Project(p.split('/')[-1], p, prj_category.split('/')[-1].lower()))
    return projects


def get_default_editor():
    with open(DEFAULT_EDITOR_FILE_PATH, 'r') as f:
        s = f.read().strip()
    return s


def set_default_editor(new_editor):
    with open(DEFAULT_EDITOR_FILE_PATH, 'w') as f:
        f.write(new_editor)
