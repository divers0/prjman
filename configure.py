import os


with open('install.sh', 'r') as f:
    install_file = f.readlines()
install_file.insert(0, f"#!{os.getenv('SHELL')}\n")


with open('install.sh', 'w') as f:
    f.write('\n'.join(install_file))
