import click
import subprocess
from .utils import colorize
from .projects import get_default_editor, set_default_editor, find_all_projects
from .config_file import get_paths


@click.command()
@click.argument('command', default=get_default_editor())
@click.option('-v', '--value')
@click.option('--change-editor', 'new_editor')
@click.option('--exclude-dir', multiple=True)
def cli(command, value, new_editor, exclude_dir):

    if new_editor:
        set_default_editor(new_editor)
        command = new_editor


    paths = get_paths()

    projects = []
    for path in paths:
        for project in find_all_projects(path, [x for x in ','.join(exclude_dir).split(',') if x != '']):
            projects.append(project)

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
        print(f"cd '{selected_project_path}'")
    else:
        print(f"cd '{selected_project_path}';{command} '{selected_project_path}'")
