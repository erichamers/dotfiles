# /usr/bin/sh

# Target config
CONFIG_DIR=$HOME"/projects/dotfiles/"
QTILE_DIR=$CONFIG_DIR"qtile/"
QUTEBROWSER_DIR=$CONFIG_DIR"qutebrowser/"
VIM_DIR=$CONFIG_DIR"vim/"
ZSH_DIR=$CONFIG_DIR"zsh/"
I3_DIR=$CONFIG_DIR"i3/"
POLYBAR_DIR=$CONFIG_DIR"polybar/"

# Source config  
ROOT_CONF=$HOME"/.config/"
QTILE_FILE=$ROOT_CONF"qtile/config.py"
QUTEBROWSER_FILE=$ROOT_CONF"qutebrowser/config.py"
VIM_FILE=$HOME"/.vimrc"
ZSH_FILE=$HOME"/.zshrc"
I3_FILE=$ROOT_CONF"/i3/config"
I3_SCRIPT1=$ROOT_CONF"/i3/launch_modules.sh"
I3_SCRIPT2=$ROOT_CONF"/i3/launch_top.sh"
POLYBAR_FILE=$ROOT_CONF"/polybar/config"
WALLPAPERS_DIR=$HOME"/Pictures/wallpapers"

sourceDirs=($CONFIG_DIR $QTILE_DIR $QUTEBROWSER_DIR $VIM_DIR $ZSH_DIR $I3_DIR $POLYBAR_DIR $WALLPAPERS_DIR)

echo "Creating folder structure"
if ! [ -d "$CONFIG_DIR" ]; then
    echo "Config directory doesn't exist yet. Creating." 
    mkdir $CONFIG_DIR -p 
fi

for dir in "${sourceDirs[@]}"
    do
        if ! [ -d "$dir" ]; then
            echo "Creating directory: $dir"
            mkdir $dir -p
        fi
done

echo "Copying files" 

echo "==== Qtile ===="
cp -f $QTILE_FILE $QTILE_DIR

echo "==== Qutebrowser ===="
cp -f $QUTEBROWSER_FILE $QUTEBROWSER_DIR

echo "==== Vim ===="
cp -f $VIM_FILE $VIM_DIR

echo "==== Zsh ===="
cp -f $ZSH_FILE $ZSH_DIR

echo "==== I3 ===="
cp -f $I3_FILE $I3_DIR
cp -f $I3_SCRIPT1 $I3_DIR
cp -f $I3_SCRIPT2 $I3_DIR

echo "==== Polybar ===="
cp -f $POLYBAR_FILE $POLYBAR_DIR

echo "==== Wallpapers ===="
cp -fr  $WALLPAPERS_DIR $CONFIG_DIR 
