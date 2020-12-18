#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export EDITOR=vim
export SCREEN_SIZE=1024x576

alias ls='ls -alh' 
alias ll='ls -l'
alias l='ls -alh'
alias copy='xclip -sel clip'
alias ssh='env TERM=xterm-256color ssh'
alias screenshot='maim -s | xclip -selection clipboard -t image/png'
alias clean='clear && source ~/.bashrc'
PS1='[\u@\h \W]\$ '

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /home/eric/.pyenv/versions/3.9.0/lib/python3.9/site-packages/powerline/bindings/bash/powerline.sh 

export PATH=$PATH:$HOME/.pyenv/versions/3.9.0/bin
