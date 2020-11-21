echo "Downloading and installing system font..."
wget --directory-prefix $HOME/Downloads https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Agave.zip
unzip $HOME/Downloads/Agave.zip -d /usr/share/fonts
rm -rf $HOME/Downloads/Agave.zip
fc-cache

echo "Setting user configurations and permissions..."
usermod -aG docker $USER
usermod -aG wheel $USER

echo "Scheduling config file routing..."
if [ "$1" == "--schedule" ]; then
    touch /var/spool/cron/eric
    cat config/crontab >> /var/spool/cron/eric
fi


