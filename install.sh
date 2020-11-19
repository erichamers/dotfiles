#!/bin/sh

PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

cp -r $PROJECT_DIR/"i3" $CONFIG_DIR
cp -r $PROJECT_DIR/"qutebrowser" $CONFIG_DIR
cp -r $PROJECT_DIR/"wallpapers" $HOME/"Pictures/wallpapers"
cp -r $PROJECT_DIR/"polybar" $CONFIG_DIR
cp -r $PROJECT_DIR/"fish" $CONFIG_DIR
cp -r $PROJECT_DIR/"vim/.vimrc" $HOME
