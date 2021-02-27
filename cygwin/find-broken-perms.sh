#!/bin/sh
#
# Find files that have had their perms blown off by a Windows app. This is
# happening when editing files with SublimeText, but not every time... I wonder
# what the trigger is?
#
# @author: https://github.com/Taffer
# @license: The MIT License (MIT), see LICENSE for details.

if [ "$1" = "--help" ]; then
    echo "$0 directory [directory2 ... directoryn]"
    echo
    echo "  Search 'directory' for files that have 000 permissions."
    exit 0
fi

for name in "$@" ; do
    if [ ! -d "$name" ] ; then
        echo "$name: not a directory"
        continue
    fi

    find "$name" -type f -print0 | xargs -0 stat -c '%a %n' | grep '^0 '
done
