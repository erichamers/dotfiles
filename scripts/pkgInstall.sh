#!/bin/bash

input=$HOME/"projects/dotfiles/pkglist.txt"
while IFS= read -r line
do
    yay -S --noconfirm $line
done < "$input"
