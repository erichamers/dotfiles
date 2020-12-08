#!/bin/bash

CONFIG_DIR=$HOME/".config"
PROJECT_DIR=$HOME/"projects/dotfiles"
PROJECT_CONFIG=$PROJECT_DIR/".config"

cp $HOME/".bashrc" $PROJECT_DIR
cp $HOME/".vimrc" $PROJECT_DIR
cp $HOME/".xinitrc" $PROJECT_DIR
cp $HOME/".zshrc" $PROJECT_DIR

cp -r $CONFIG_DIR/"alacritty/" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"color-scripts" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"i3" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"picom" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"polybar" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"qtile" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"qutebrowser" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"rofi" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"wallpapers" $PROJECT_CONFIG
cp -r $CONFIG_DIR/"dunst" $PROJECT_CONFIG
