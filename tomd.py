#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2014 maxint <NOT_SPAM_lnychina@gmail.com>
# Distributed under terms of the MIT license.

"""

"""

import json
import codecs


def main(src, dst):
    book = json.load(open(src, 'rt'))
    with codecs.open(dst, 'wt', encoding='utf-8') as fp:
        def write(s):
            fp.write(s)

        write(u'% {}\n'.format(book['title']))
        write(u'% {}\n'.format(book['author']))
        write(u'\n\n')
        write(book['summary'])
        write(u'\n\n')
        start_idx = 0
        end_idx = 0
        sections = book['sections']
        for majors in book['major_sections']:
            write(u'# {}'.format(majors['name']))
            end_idx += majors['num']
            for i in range(start_idx, end_idx):
                section = sections[i]
                write(u'\n\n')
                write(u'## {}'.format(section['subtitle']))
                write(u'\n\n')
                write(section['content'].replace('\r\n', '\n'))

if __name__ == '__main__':
    import os.path
    import argparse

    parser = argparse.ArgumentParser(description='Convert to MarkDown format')
    parser.add_argument('input',
                        help='Input json file')
    parser.add_argument('--output', '-o', nargs='?', default=None,
                        help='Output MarkDown file')

    args = parser.parse_args()

    if args.output is None:
        args.output = os.path.splitext(args.input)[0] + '.md'

    main(args.input, args.output)
    # main('santi/三体.json', 'test.md')
