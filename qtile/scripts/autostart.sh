#!/bin/sh

killall picom
sleep 1
picom -b &
