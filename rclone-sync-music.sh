#!/bin/sh
if [ ! -e /mnt/rust/Music ] ; then
    echo '"rust" drive not mounted'
    exit 1
fi

rclone sync /mnt/rust/Music b2:vanguard-music-archive --bwlimit "08:00,1M 12:00,2M 13:00,1M 22:00,off" --progress
