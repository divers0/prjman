import os
import click
import subprocess
from .projects import get_default_editor, set_default_editor, find_all_projects, colorize


@click.command()
@click.argument('editor', default=get_default_editor())
@click.option('-v', '--value')
@click.option('--change-editor', 'new_editor')
def cli(editor, value, new_editor):

    if new_editor:
        set_default_editor(new_editor)
        editor = new_editor

    projects = find_all_projects()
    projects_names = '\n'.join(sorted([colorize(projects[x].name, 'green')+' '*(len(sorted([x.name for x in projects], key=lambda x: len(x), reverse=True)[0]+' ')-len(projects[x].name))+colorize(projects[x].path, 'blue') for x, _ in enumerate(projects)]))



    # command = f"""cat > /tmp/source << EOF
# {projects_names}
# EOF

# perl -pe 'BEGIN{{undef $/;}} s/\\n\\n/\\x0/g; s/\n$//g' /tmp/source |
  # fzf --ansi --height 70% --reverse --read0 --no-hscroll --preview "echo {{}}" --preview-window up:2 --info=inline --border --margin=1 --padding=1 --color bg:#222222,preview-bg:#333333"""

  # BACKUP TO THE OLD COMMAND's LAST LINE
  # fzf --ansi --height 70% --reverse --read0 --no-hscroll --preview "echo {{}}" --preview-window up:2 --info=inline --border --margin=1 --padding=1 --color bg:#222222,preview-bg:#333333"""

    fzf_args = ["--ansi", "--height 70%", "--reverse", "--no-hscroll", "--border", "--margin=1", "--padding=1", "--color bg:#222222"]
    if value:
        fzf_args.append(f'-q {value}')
    command = f"echo '{projects_names}' | fzf {' '.join(fzf_args)}"

    try:
        command_output = subprocess.check_output(command, shell=True).decode('utf-8')
    except subprocess.CalledProcessError:
        return

    selected_project_path = command_output.split()[1].strip()

    os.system(f"{editor} '{selected_project_path}'")

