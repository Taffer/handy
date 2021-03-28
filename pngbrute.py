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
        self.filename = filename
        self.level = level

    def run(self):
        crushed_name = '{1}-{0}.crushed'.format(self.level, self.filename)
        print('Crushing {1} for level {0} -> {2}'.format(self.level, self.filename, crushed_name))
        os.system('pngcrush -brute -l {0} {1} {2} > /dev/null 2>&1'.format(self.level, self.filename, crushed_name))
        orig_size = os.path.getsize(self.filename)
        new_size = os.path.getsize(crushed_name)
        if new_size == 0 or new_size >= orig_size:
            os.unlink(crushed_name)


def crush(filename):
    crushers = [Crusher(filename, z) for z in range(1, 10)]
    for t in crushers:
        t.start()

    for t in crushers:
        t.join()

    orig_size = os.path.getsize(filename)
    best_size = orig_size
    winner = 0
    for z in range(1, 10):
        crushed_name = '{0}-{1}.crushed'.format(filename, z)
        crushed_size = os.path.getsize(crushed_name)
        if crushed_size > 0 and crushed_size < best_size:
            if winner != 0:
                os.unlink('{0}-{1}.crushed'.format(filename, winner))
            winner = z
            best_size = crushed_size
        else:
            os.unlink(crushed_name)

    shutil.move(filename, filename + '.orig')
    os.rename('{0}-{1}.crushed'.format(filename, winner), filename)


def main(args):
    for file in args:
        crush(file)


if __name__ == '__main__':
    main(sys.argv[1:])
