#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then exec startx; fi

alias ls='ls --color=auto'
alias ll='ls -l'
alias l='ls -lah'
PS1='[\u@\h \W]\$ '
