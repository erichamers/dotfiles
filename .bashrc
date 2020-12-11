#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export EDITOR=vim
export SCREEN_SIZE=1024x576

alias ls='ls --color=auto'
alias ll='ls -l'
alias l='ls -alh'
alias copy='xclip -sel clip'
alias ssh='env TERM=xterm-256color ssh'
PS1='[\u@\h \W]\$ '
