#!/bin/sh
#
# Launch Sublime Text from a Cygwin shell.

# If we don't split out the args, cygpath will eat them.
ARGS=""
for arg in "$@" ; do
    case $arg in
        -*)
            ARGS="$ARGS $arg"
            shift
            ;;
    esac
done

for i in "$@" ; do
    "/cygdrive/c/Program Files/Sublime Text 3/subl.exe" $ARGS "$(cygpath --mixed "$i")"
done
