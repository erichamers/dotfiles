#!/bin/bash

PROJECT_DIR=$HOME'/projects/dotfiles'

echo "Installing packages"

sudo pacman -Syy --noconfirm

sudo pacman -S xorg \
               xorg-xinit \
               python-pip \
               nitrogen \
               nvidia \
               picom \
               alsa-utils \
               pulseaudio \
               pulseaudio-alsa \
               pyenv \
               docker \
               wget \
               curl \
               ranger \
               rofi \
               qutebrowser \
               mlocate \
               base-devel \
               xterm \
               weechat \
               go \
               xclip \
               wmctrl \
               cronie \
               dunst \
               epdfview \
               neofetch \
               ueberzug \
               unclutter \
               unzip \
               pango \
               virtualbox \
               virtualbox-host-modules-arch \
               virtualbox-guest-iso \
               python-dbus \
               python-gobject \
               libnotify \
               powerline \
               powerline-fonts \
               openssh \
               openvpn --noconfirm 

sudo usermod -aG docker eric
sudo modprobe vboxdrv

pyenv install 3.9.0
pyenv global 3.9.0 

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> $HOME"/.bashrc"
echo 'eval "$(pyenv init -)"' >> $HOME"/.bashrc"

source $HOME'/.bashrc'

pip install wheel setuptools

echo "Installing yay"
sudo git clone https://aur.archlinux.org/yay-git.git /opt/yay-git \
    && sudo chown -R eric:eric /opt/yay-git

cd /opt/yay-git && makepkg -si --noconfirm && cd $PROJECT_DIR

yay -Syy --noconfirm

echo "Installing yay packages"

yay -S visual-studio-code-bin \
       skypeforlinux-stable-bin \
       slack-desktop \ 
       powerline-vim \
       qtile-git \
       timeshift --noconfirm

echo "Installing ST terminal"
git clone https://github.com/erichamers/st $HOME'/apps/st'
cd $HOME'/apps/st' && sudo make clean install && cd $PROJECT_DIR

sudo mkdir /usr/share/fonts/mononoki
sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Mononoki.zip -P /usr/share/fonts/mononoki
sudo unzip /usr/share/fonts/mononoki/Mononoki.zip
fc-cache

echo "Installing configuration files" 

dotfiles=( $(find . -type f -name '.*') )

for file in "${dotfiles[@]}" 
do
    cp $file $HOME
done

source $HOME'/.bashrc'

cp -r $PROJECT_DIR'/.config/' $HOME
