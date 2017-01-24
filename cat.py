#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import os
import fnmatch


# noinspection PyShadowingBuiltins
def file(name, indent=0):
    ind, ret = ' ' * indent, []
    with open(name, 'rt') as fin:
        for ln in fin:
            ret.append('{0}{1}'.format(ind, ln.rstrip('\r\n')))
    return ret


def directory(name, recurse=False, indent=0, file_filter='*', dir_filter='*'):
    ret = []
    for root, dirs, files in os.walk(name):
        root_base = os.path.basename(root)
        if not fnmatch.fnmatch(root_base, dir_filter):
            continue
        for fn in files:
            if fnmatch.fnmatch(fn, file_filter):
                ret.extend(file(os.path.join(root, fn), indent=indent))
        if not recurse:
            break
    return ret
