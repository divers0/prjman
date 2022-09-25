if [[ $SHELL == "/bin/zsh" ]]; then
	rc="$HOME/.zshrc"
elif [[ $SHELL == "/bin/bash" ]]; then
	rc="$HOME/.bashrc"
elif [[ $SHELL == "/bin/fish" ]]; then
	rc="$HOME/.config/fish/config.fish"
fi

source $rc

if [[ ! "$(alias prjman)" == "" || ! "$(type prjman)" == *"not found"* ]];then
    echo "prjman has not been uninstalled properly and it still exists in your shellrc file.\nplease uninstall it and try again."
    exit 1
fi
pip install . > /dev/null


cat $rc
