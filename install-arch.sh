#!/bin/sh

HOME=~eric
PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

echo "Creating folder structure..."
mkdir $HOME/projects $HOME/apps $CONFIG_DIR/picom

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
    pcmanfm

echo "Setting user configurations and permissions..."
usermod -aG docker $USER
usermod -aG wheel $USER

echo "Installing polybar..."
yay -S polybar skypeforlinux-stable-bin visual-studio-code-bin

echo "Downloading and installing system font..."
wget --directory-prefix $HOME/Downloads https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Agave.zip
unzip $HOME/Downloads/Agave.zip -d /usr/share/fonts
rm -rf $HOME/Downloads/Agave.zip
fc-cache

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

echo "Scheduling config file routing..."
if [ "$1" == "--schedule" ]; then
    touch /var/spool/cron/eric
    cat config/crontab >> /var/spool/cron/eric
fi

echo "Installation complete!"
