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
XINIT_FILE=$HOME/".xinitrc"
BASH_FILE=$HOME/".bashrc"
BASH_PROFILE=$HOME/".bash_profile"
COLORS_DIR=$CONFIG_DIR"/color-scripts"
ALACRITTY_DIR=$CONFIG_DIR"/alacritty"

cp -rp $I3_DIR $PROJECT_DIR
cp -rp $QUTEBROWSER_DIR $PROJECT_DIR
cp -rp $WALLPAPERS_DIR $PROJECT_DIR
cp -rp $FISH_DIR $PROJECT_DIR
cp -rp $POLYBAR_DIR $PROJECT_DIR
cp -rp $PICOM_DIR $PROJECT_DIR
cp -rp $COLORS_DIR $PROJECT_DIR
cp -rp $ALACRITTY_DIR $PROJECT_DIR
cp $VIM_FILE $PROJECT_DIR/"vim/.vimrc"
cp $XINIT_FILE $PROJECT_DIR/"xinit/.xinitrc"
cp $BASH_FILE $PROJECT_DIR/"bash/.bashrc"
cp $BASH_PROFILE $PROJECT_DIR/"bash/.bash_profile"

mkdir -p $PROJECT_DIR/"vim" && cp -r $VIM_FILE $PROJECT_DIR/"vim/"
