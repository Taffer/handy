#! /usr/bin/env python3
#
# Use threads to speed up pngcrush brute force operations.

import threading
import os
import os.path
import shutil
import sys


class Crusher(threading.Thread):
    def __init__(self, filename, level):
        threading.Thread.__init__(self)
        self.name = '{0}-{1}'.format(filename, level)
        self.crushed_name = self.name + '.crushed'
        self.filename = filename
        self.level = level

    def run(self):
        os.system('pngcrush -brute -l {0} {1} {2} > /dev/null 2>&1'.format(self.level, self.filename, self.crushed_name))


def crush(filename):
    crushers = [Crusher(filename, z) for z in range(1, 10)]
    for t in crushers:
        t.start()

    for t in crushers:
        t.join()

    orig_size = os.path.getsize(filename)
    best_size = orig_size
    winner = None

    for c in crushers:
        crushed_size = os.path.getsize(c.crushed_name)
        if crushed_size == 0:
            os.unlink(c.crushed_name)
            continue

        if crushed_size < best_size:
            if winner is not None:
                os.unlink(winner.crushed_name)
            winner = c
            best_size = crushed_size
        else:
            os.unlink(c.crushed_name)

    if winner is not None:
        shutil.move(filename, filename + '.orig')
        os.rename(winner.crushed_name, filename)


def main(args):
    for file in args:
        crush(file)


if __name__ == '__main__':
    main(sys.argv[1:])
