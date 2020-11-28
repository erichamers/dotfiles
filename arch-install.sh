#!/bin/sh

# Author: Eric Hamers (erichamers@gmail.com)
# This is the installation file for my arch linux i3 environment.

HOME=~eric
PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

echo "Creating folder structure..."
mkdir $HOME/projects $HOME/apps $CONFIG_DIR/picom $HOME/fonts $HOME/.ssh

echo "Installing Vundle plugin manager for vim..."
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

git config --global user.name "erichamers"
git config --global user.email "erichamers@gmail.com"

echo "Installing powerline fonts..."
git clone https://github.com/powerline/fonts ~/fonts/
cd $HOME/fonts/ && ./install.sh

echo "Installing basic packages..." 
yay -S qutebrowser \
    rofi \
    picom \
    powerline-vim \
    pyenv \
    nitrogen \
    unzip \
    wget \
    docker \
    gvim \
    neofetch \
    unclutter \
    pcmanfm \
    xclip \
    polybar \
    skypeforlinux-stable-bin \
    visual-studio-code-bin

echo "Installing Python..."
pyenv install 3.8.6
pyenv global 3.8.6

echo "Setting config files..."
cp -r $PROJECT_DIR/"i3" $CONFIG_DIR
cp -r $PROJECT_DIR/"qutebrowser" $CONFIG_DIR
cp -r $PROJECT_DIR/"wallpapers/*" $HOME/"Pictures/wallpapers"
cp -r $PROJECT_DIR/"polybar" $CONFIG_DIR
# cp -r $PROJECT_DIR/"fish" $CONFIG_DIR
cp -r $PROJECT_DIR/"vim/.vimrc" $HOME
cp -r $PROJECT_DIR/"color-scripts" $CONFIG_DIR
cp -r $PROJECT_DIR/"alacritty" $CONFIG_DIR
cp -r $PROJECT_DIR/"picom" $CONFIG_DIR
cp -r $PROJECT_DIR/"xinit/.xinitrc" $HOME
cp -r $PROJECT_DIR/"bash/.bashrc" $HOME/".bashrc"
cp -r $PROJECT_DIR/"bash/.bash_profile" $HOME/".bash_profile"

echo "Installation complete!"
