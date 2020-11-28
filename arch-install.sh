#!/bin/sh

# Author: Eric Hamers (erichamers@gmail.com)
# This is the installation file for my arch linux i3-gaps environment.
# It assumes that the instalation was done via zen-installer and a couple of 
# applications are preinstalled.
# Preinstalled applications that might be relative to this installation file
# are: 
#   - fish
#   - yay
#   - git
# plus some other base applications and firmware

HOME=~eric
PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

echo "Creating folder structure..."
mkdir $HOME/projects $HOME/apps $CONFIG_DIR/picom $HOME/fonts $HOME/.ssh

yay -S openssh
ssh-keygen -t ed25519 -C "erichamers@gmail.com" -N '' -f $HOME/.ssh/id_ed25519
eval "$(ssh-agent -s)"
ssh-add $HOME/.ssh/id_ed25519

echo "Installing Vundle plugin manager for vim..."
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

git config --global user.name "erichamers"
git config --global user.email "erichamers@gmail.com"

echo "Installing powerline fonts..."
git clone https://github.com/powerline/fonts ~/fonts/
cd $HOME/fonts/ && ./install.sh

echo "Installing basic packages..." 
yay -S qutebrowser \
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
cp -r $PROJECT_DIR/"wallpapers" $HOME/"Pictures/wallpapers"
cp -r $PROJECT_DIR/"polybar" $CONFIG_DIR
cp -r $PROJECT_DIR/"fish" $CONFIG_DIR
cp -r $PROJECT_DIR/"vim/.vimrc" $HOME
cp -r $PROJECT_DIR/"color-scripts" $CONFIG_DIR
cp -r $PROJECT_DIR/"alacritty" $CONFIG_DIR
cp -r $PROJECT_DIR/"picom" $CONFIG_DIR

echo "Customizing alacritty..."
curl https://raw.githubusercontent.com/dracula/alacritty/master/dracula.yml >> $CONFIG_DIR/alacritty/alacritty.yml

echo "Installation complete!"
