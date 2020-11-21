#!/bin/sh

HOME=~eric
PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

echo "Creating folder structure..."
mkdir $HOME/projects $HOME/apps $CONFIG_DIR/picom $HOME/.ssh

echo "Installing Vundle plugin manager for vim..."
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

git config --global user.name "erichamers"
git config --global user.email "erichamers@gmail.com"

echo "Installing basic packages..." 
pacman -S qutebrowser \
    picom \
    alacritty \
    powerline \
    powerline-vim \
    powerline-fonts \
    pyenv \
    nitrogen \
    unzip \
    wget \
    docker \
    gvim \
    neofetch \
    unclutter \
    pcmanfm \
    xclip

echo "Installing polybar..."
yay -S polybar skypeforlinux-stable-bin visual-studio-code-bin

echo "Installing Python..."
pyenv install 3.8.6
pyenv global 3.8.6

echo "Setting config files..."
cp -r $PROJECT_DIR/"i3" $CONFIG_DIR
cp -r $PROJECT_DIR/"qutebrowser" $CONFIG_DIR
cp -r $PROJECT_DIR/"wallpapers" $HOME/"Pictures/wallpapers"
cp -r $PROJECT_DIR/"polybar" $CONFIG_DIR
cp -r $PROJECT_DIR/"fish" $CONFIG_DIR
cp -r $PROJECT_DIR/"vim/.vimrc" $HOME
cp -r $PROJECT_DIR/"color-scripts" $CONFIG_DIR

echo "Installation complete!"
