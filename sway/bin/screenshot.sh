#!/bin/bash

if [ "$1" == "-f" ]; then
    mkdir -p $HOME/Pictures/Screenshots/$(date +%Y-%m) && grim /tmp/scr.png && wl-copy --type image/png < /tmp/scr.png && cp /tmp/scr.png $HOME/Pictures/Screenshots/$(date +%Y-%m)/$(date +%d-%H-%M-%S-%N).png && notify-send -t 500 "click"
else
    mkdir -p $HOME/Pictures/Screenshots/$(date +%Y-%m) && slurp | grim -g- /tmp/scr.png && wl-copy --type image/png < /tmp/scr.png && cp /tmp/scr.png $HOME/Pictures/Screenshots/$(date +%Y-%m)/$(date +%d-%H-%M-%S-%N).png && notify-send -t 500 "click"
fi
