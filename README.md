## Setup Files

This is the repository with the basic setup files for my linux environment.

As time goes by, there are applications that I no longer use and new ones that are getting added as I discover or need.

### How to use this script

There are 3 bash scripts in this project that allow you to pull the files from their respective folders, to push it to
github and to install it in the proper locations.

To run the scripts, all you need to do is execute `./pull.sh` to pull all the config files from their respective folders
, then run `./push.sh` to push it to github and `./install.sh` to install all the files in their respective folders.

The installation will also include the tasks on crontab to execute pull and push daily.

You can configure the scheduling by editing the `crontab` file in the config directory and you also need set the user in
the `install.sh` script and run it with sudo and using the flag `--schedule`, it would look something like this:
```bash
sudo ./install.sh --schedule
```

**Current environment:**

![workspace](https://i.imgur.com/bb9ASRb.jpg)

- Arch Linux
- i3 Window Manager
- Polybar Status Bar

Utilities:
- Fish shell
- qutebrowser
- vim
