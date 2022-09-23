#!/bin/sh


pip install .

if [ $SHELL == "/bin/zsh" ]; then
  rc="$HOME/.zshrc"
elif [ $SHELL == "/bin/bash" ]; then
  rc="$HOME/.bashrc"
elif [ $SHELL == "/bin/fish" ]; then
  rc="$HOME/.config/fish/config.fish"
fi

eval "$SHELL $rc"
