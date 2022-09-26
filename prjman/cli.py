import os
import subprocess

import click

from .config_file import add_to_paths, get_paths
from .projects import find_all_projects, get_default_editor, set_default_editor
from .utils import colorize, validate_multi_value_options


@click.command()
@click.argument("command", default=get_default_editor())
@click.option("-v", "--value")
@click.option("-a", "--add-path", multiple=True)
@click.option("--change-editor", "new_editor")
@click.option("-i", "--include-dir", multiple=True)
@click.option("-x", "--exclude-dir", multiple=True)
def cli(command, value, add_path, new_editor, include_dir, exclude_dir):

    if new_editor:
        set_default_editor(new_editor)
        command = new_editor

    if add_path:
        new_paths = validate_multi_value_options(add_path)
        for new_path in new_paths:
            if not os.path.isdir(new_path):
                print(f"'{new_path}' is not a directory.")
                return
        add_to_paths(new_paths)

    paths = get_paths()
    projects = []

    # Adding include_dirs
    for include in validate_multi_value_options(include_dir):
        for prj_dir in os.listdir(include):
            projects.append((prj_dir, os.path.join(include, prj_dir)))

    for path in paths:
        for project in find_all_projects(
            path, validate_multi_value_options(exclude_dir)
        ):
            projects.append(project)

    # Removing duplicates
    projects = list(set(projects))

    # If you think this is trash code you are trash
    projects_names = '\n'.join(sorted([colorize(projects[x][0], 'green')+' '*(len(sorted([x[0] for x in projects], key=lambda x: len(x), reverse=True)[0]+' ')-len(projects[x][0]))+colorize(projects[x][1], 'blue') for x, _ in enumerate(projects)]))

    fzf_args = [
        "--ansi",
        "--height 70%",
        "--reverse",
        "--no-hscroll",
        "--border",
        "--margin=1",
        "--padding=1",
        "--color bg:#222222",
    ]
    if value:
        fzf_args.append(f"-q {value}")
    fzf_command = f"echo '{projects_names}' | fzf {' '.join(fzf_args)}"

    try:
        fzf_command_output = subprocess.check_output(
            fzf_command, shell=True).decode("utf-8"
        )
    except subprocess.CalledProcessError:
        return

    selected_project_path = fzf_command_output.split()[1].strip()

    if command == "cd":
        print(f"cd '{selected_project_path}'")
    else:
        print(f"cd '{selected_project_path}';{command} '{selected_project_path}'")
