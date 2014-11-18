#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (C) 2014 maxint <NOT_SPAM_lnychina@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Convert markdown / json file to ebook.
"""

import os.path
import subprocess


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Make ebook')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('--output', '-o', nargs='?', default=None,
                        help='Output ebook file')

    args = parser.parse_args()

    name, ext = os.path.splitext(args.input)
    ext = ext.lower()
    assert ext in ['.md', '.json'], 'Unsupported format of input file'

    if args.output is None:
        args.output = name + '.epub'

    if ext == '.json':
        import tomd
        mdpath = name + '.md'
        tomd.main(args.input, mdpath)
        args.input = mdpath

    cmd = 'pandoc {} -o {}'.format(args.input, args.output)
    subprocess.check_call(cmd)
