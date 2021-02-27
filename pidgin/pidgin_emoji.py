#!/usr/bin/python2.7
''' Generate an emoji text replacement list for Pidgin.

This needs Taehoon Kim's "emoji" module, which can be installed with pip:

pip install emoji

Append the output to your ~/.purple/dict file; on Windows, the dict file
is found in %APP_DATA%/.purple/dict.

Created on Nov 29, 2014

@author: https://github.com/Taffer
@license: The MIT License (MIT), see LICENSE for details.
'''

from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import emoji
import sys


def emoji2pidgin():
    ''' Convert the Emoji tokens as Pidgin dictionary entries. '''
    pidgin_dict = '\nCOMPLETE 1\nCASE 1\nBAD {0}\nGOOD {1}\n'

    entries = [pidgin_dict.format(k, emoji.code.emojiCodeDict[k]) for k in emoji.code.emojiCodeDict]

    return entries


def main():
    ''' Dump the Emjoi dictionary entries to stdout. '''
    parser = argparse.ArgumentParser(description='Generate an emoji dictionary for Pidgin. :thumbsup:')
    parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                        help='Send output to the given file; default is stdout.')
    args = parser.parse_args()

    pidgin_entries = emoji2pidgin()

    for entry in pidgin_entries:
        args.output.write(entry.encode('utf-8'))


if __name__ == '__main__':
    main()
