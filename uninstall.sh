#!/bin/bash


rm -rf ~/.config/prjman
pip uninstall prjman
FIRST_STR="prjman() {\n    projman\n}"
SECOND_STR="prjman() {\n    eval \$(projman \"\$@\")\n}"

if [ $SHELL == "/bin/zsh" ]; then
  RC_FILE_PATH="$HOME/.zshrc"
elif [ $SHELL == "/bin/bash" ]; then
  RC_FILE_PATH="$HOME/.bashrc"
elif [ $SHELL == "/bin/fish" ]; then
  RC_FILE_PATH="$HOME/.config/fish/config.fish"
fi

RC_FILE_CONTENT=$(cat "$RC_FILE_PATH")

FIRST_STR_IN_RC=$(python -c "print('$FIRST_STR' in '''$RC_FILE_CONTENT''')")
SECOND_STR_IN_RC=$(python -c "print('$SECOND_STR' in '''$RC_FILE_CONTENT''')")

if [[ "$FIRST_STR_IN_RC" == "True" ]]; then
    sed -z "s/$FIRST_STR//g" "$RC_FILE_PATH" > "$RC_FILE_PATH"
elif [[ "$SECOND_STR_IN_RC" == "True" ]]; then
    sed -z "s/$SECOND_STR//g" "$RC_FILE_PATH" > "$RC_FILE_PATH"
fi
