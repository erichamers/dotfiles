# /usr/bin/bash

# Target config
CONFIG_DIR=$HOME"/projects/dotfiles/"
QTILE_DIR=$CONFIG_DIR"qtile/"
QUTEBROWSER_DIR=$CONFIG_DIR"qutebrowser/"
VIM_DIR=$CONFIG_DIR"vim/"
ZSH_DIR=$CONFIG_DIR"zsh/"

# Source config  
ROOT_CONF=$HOME"/.config/"
QTILE_FILE=$ROOT_CONF"qtile/config.py"
QUTEBROWSER_FILE=$ROOT_CONF"qutebrowser/config.py"
VIM_FILE=$HOME"/.vimrc"
ZSH_FILE=$HOME"/.zshrc"

sourceDirs=($CONFIG_DIR $QTILE_DIR $QUTEBROWSER_DIR $VIM_DIR $ZSH_DIR)

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
