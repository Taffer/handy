#! /bin/sh
#
# Mimic MacOS's "open" command.

exec xdg-open "$@" > /dev/null 2>&1
