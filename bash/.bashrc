#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -l'
alias l='ls -alh'
alias copy='xclip -sel clip'
PS1='[\u@\h \W]\$ '
