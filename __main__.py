#! /usr/bin/python
'''
    __main__.py
    Generate themes from .Xresources
'''
import argparse
from os import path

import xresparser
from renderer import render_template, render_all


def parse_args():
    '''
    Parse command line arguments
    '''

    parser = argparse.ArgumentParser(
        description='Generate themes from .Xresources')

    parser.add_argument(
        '-i',
        action='store',
        default=path.join(path.expanduser('~'), '.Xresources'),
        dest='xres_file',
        help='input file -- If not specified it will try to use ~/.Xresources')

    parser.add_argument(
        '-o',
        action='store',
        default=path.join(path.expanduser('~'), '.config', 'theme-gen', 'themes'),
        dest='output_dir',
        help='output directory -- If not specified it will try to use ~/.config/theme-gen')

    # Check if there's a user templates directory
    tpl_dir = path.join(path.expanduser('~'), '.config', 'theme-gen', 'templates')
    if not path.isdir(tpl_dir):
        tpl_dir = path.join(path.dirname(__file__), 'templates')

    parser.add_argument(
        '-t',
        action='store',
        default=tpl_dir,
        dest='tpl_dir',
        help='templates directory -- If not specified it will try to use ./templates')

    parsed = parser.parse_args()

    return parsed


if __name__ == "__main__":
    args = parse_args()
    xresources = xresparser.parse(args.xres_file)

    # Render all templates
    render_all(
        args.tpl_dir,
        args.output_dir,
        xresources
    )
