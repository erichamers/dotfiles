#!/bin/sh

# If you are running this script with the --schedule flag you 
# should run it with sudo

HOME=~eric
PROJECT_DIR=$HOME/"projects/dotfiles"
CONFIG_DIR=$HOME/".config"

cp -r $PROJECT_DIR/"i3" $CONFIG_DIR
cp -r $PROJECT_DIR/"qutebrowser" $CONFIG_DIR
cp -r $PROJECT_DIR/"wallpapers" $HOME/"Pictures/wallpapers"
cp -r $PROJECT_DIR/"polybar" $CONFIG_DIR
cp -r $PROJECT_DIR/"fish" $CONFIG_DIR
cp -r $PROJECT_DIR/"vim/.vimrc" $HOME
cp -r $PROJECT_DIR/"color-scripts" $CONFIG_DIR

if [ "$1" == "--schedule" ]; then
    cat config/crontab >> /var/spool/cron/eric
fi
