import os
import click
import subprocess
from .utils import colorize, copy_to_clipboard
from .projects import get_default_editor, set_default_editor, find_all_projects


@click.command()
@click.argument('command', default=get_default_editor())
@click.option('-v', '--value')
@click.option('--change-editor', 'new_editor')
def cli(command, value, new_editor):

    if new_editor:
        set_default_editor(new_editor)
        editor = new_editor

    projects = find_all_projects()
    projects_names = '\n'.join(sorted([colorize(projects[x].name, 'green')+' '*(len(sorted([x.name for x in projects], key=lambda x: len(x), reverse=True)[0]+' ')-len(projects[x].name))+colorize(projects[x].path, 'blue') for x, _ in enumerate(projects)]))

    fzf_args = ["--ansi", "--height 70%", "--reverse", "--no-hscroll", "--border", "--margin=1", "--padding=1", "--color bg:#222222"]
    if value:
        fzf_args.append(f'-q {value}')
    fzf_command = f"echo '{projects_names}' | fzf {' '.join(fzf_args)}"

    try:
        fzf_command_output = subprocess.check_output(fzf_command, shell=True).decode('utf-8')
    except subprocess.CalledProcessError:
        return

    selected_project_path = fzf_command_output.split()[1].strip()

    if command == 'cd':
        copy_to_clipboard(f"cd \"{selected_project_path}\"")
        print(f"The command 'cd {selected_project_path}'"
              " has been copied to clipboard.")
    else:
        os.system(f"{command} '{selected_project_path}'")
