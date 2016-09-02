#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function

import os

import requests
from lxml import html


BASE_URL = 'https://www.quantifiedcode.com{path}'


def get(path):
    url = BASE_URL.format(path=requests.utils.unquote(path))
    page = requests.get(url)
    page.encoding = 'utf-8'
    return page


def save_page(path):
    page = get(path)
    fs_path = requests.utils.unquote(path[1:])
    fs_path_parts = fs_path.split('/')
    dir_path, file_path = fs_path_parts[:-1], fs_path_parts[-1]
    os.makedirs(os.sep.join(dir_path), exist_ok=True)
    fname = os.sep.join(fs_path_parts) + '.html'
    with open(fname, 'w') as f:
        f.write(page.text)



def main():
    kb = 'knowledge-base'
    os.makedirs(kb, exist_ok=True)
    page = get('/{}'.format(kb))
    tree = html.fromstring(page.text)
    anchor = tree.get_element_by_id('python')
    assert anchor.tag == 'a'
    uls = anchor.itersiblings('ul')

    for ul in uls:
        links = ul.xpath('li/a')
        for link in links:
            path = link.attrib.get('href', '')
            assert path.startswith('/')

            save_page(path)


if __name__ == '__main__':
    main()
