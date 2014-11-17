#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2014 maxint <NOT_SPAM_lnychina@gmail.com>
# Distributed under terms of the MIT license.

"""

"""
import requests
import lxml.etree
import urlparse
import json
from collections import OrderedDict
import re


def get_etree(r):
    #from lxml.html.clean import Cleaner
    #cleaner = Cleaner(style=True,
                      #scripts=True,
                      #safe_attrs_only=True)
    #html = cleaner.clean_html(r.content.decode('gbk'))
    html = r.content.decode('gbk')
    #print html.encode('utf-8')
    return lxml.etree.HTML(html)


def fetch_content(url):
    print 'Downloading {}'.format(url)
    # return url
    r = requests.get(url)
    dom = get_etree(r)
    elements = dom.xpath(u'/html/body/div[1]/table[5]//tr[1]/td[2]/p/child::text()')
    s = ''.join(elements)
    #import ipdb; ipdb.set_trace()
    return s


def get_author_date(dom):
    s = dom.xpath(u'/html/body/table[3]/tr[2]/td')[0].text
    m = re.search(u'\uff1a(\S+).*\uff1a(\S+)', s)
    return m.group(1), m.group(2)


def get_major_sections(dom):
    major_trs = dom.xpath(u'/html/body/table[3]//table[2]//tr[@align="center"]')
    sections = list()
    for tr in major_trs:
        name = tr.xpath(u'child::td//child::text()')[0]
        t = tr.xpath(u'following-sibling::tr/child::td/child::a')
        sections.append(OrderedDict(name=name,
                                    num=len(t)))
    for i in range(0,len(sections)-1):
        sections[i]['num'] -= sections[i+1]['num']
    return sections



def main(url):
    r = requests.get(url)
    dom = get_etree(r)
    title = dom.xpath(u'//table[3]//tr[1]//h1//font')[0].text
    author, date = get_author_date(dom)
    summary = dom.xpath(u'/html/body/table[3]//table[1]//tr[2]/td/child::text()')[0].strip()
    print 'Title:', title.encode('utf-8')
    print 'Author:', author.encode('utf-8')
    print 'Date:', date.encode('utf-8')
    print 'Summary:', summary
    elements = dom.xpath(u'/html/body/table[3]//table[2]//tr//a')
    book = OrderedDict(title=title,
                       author=author,
                       date=date,
                       summary=summary,
                       major_sections=get_major_sections(dom))
    sections = list()
    for elem in elements:
        link = elem.values()[0]
        subtitle = elem.text
        suburl = urlparse.urljoin(url, link)
        print 'Section:', subtitle.encode('utf-8')
        content = fetch_content(suburl)
        sections.append(OrderedDict(subtitle=subtitle, content=content))
    with open(title + '.json', 'wt') as fp:
        book['sections'] = sections
        fp.write(json.dumps(book,
                            ensure_ascii=False,
                            indent=2).encode('utf-8'))
    print 'Done!'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download diction as json format')
    parser.add_argument('url', help='Target URL')

    args = parser.parse_args()
    main(args.url)

    # main('http://book.kanunu.org/book3/6630/')
    # main('http://book.kanunu.org/book3/6632/')
    # main('http://book.kanunu.org/book3/6656/')
