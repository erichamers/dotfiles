#!/bin/sh

# Base directories definition
CONFIG_DIR=$HOME/".config"
PROJECT_DIR=$HOME/"projects/dotfiles"

# System config files and directories locations
I3_DIR=$CONFIG_DIR/"i3"
QUTEBROWSER_DIR=$CONFIG_DIR/"qutebrowser"
WALLPAPERS_DIR=$HOME/"Pictures/wallpapers"
PICOM_DIR=$CONFIG_DIR/"picom"
POLYBAR_DIR=$CONFIG_DIR/"polybar"
FISH_DIR=$CONFIG_DIR/"fish"
VIM_FILE=$HOME/".vimrc"
COLORS_DIR=$CONFIG_DIR"/color-scripts"
ALACRITTY_DIR=$CONFIG_DIR"/alacritty"

cp -r $I3_DIR $PROJECT_DIR
cp -r $QUTEBROWSER_DIR $PROJECT_DIR
cp -r $WALLPAPERS_DIR $PROJECT_DIR
cp -r $FISH_DIR $PROJECT_DIR
cp -r $POLYBAR_DIR $PROJECT_DIR
cp -r $PICOM_DIR $PROJECT_DIR
cp -r $COLORS_DIR $PROJECT_DIR
cp -r $ALACRITTY_DIR $PROJECT_DIR

mkdir -p $PROJECT_DIR/"vim" && cp -r $VIM_FILE $PROJECT_DIR/"vim/"
