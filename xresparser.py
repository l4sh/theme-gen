'''
    xresparser.py
    Parse .Xresources files
'''
from os import path
import string


def include(filename):
    '''
    Check if include file exists and parse
    '''
    if not path.exists(filename):
        # return
        pass

    f = open(filename)

    return parse(f)


def parse(xres_file):
    '''
    Parse .Xresources file along with any include
    '''
    try:
        lines = xres_file.readlines()
    except AttributeError:
        xres_file = open(xres_file)
        lines = xres_file.readlines()

    parsed = {}
    defined = {}  # strings that start with #define

    for line in lines:
        line = line.strip()

        # Strip comments
        if not line or line.startswith('!'):
            continue

        # Parse include files
        if line.startswith('#include'):
            included = include(
                path.join(
                    path.dirname(xres_file.name),
                    line.split()[1].strip('\'"')
                )
            )

            if not included:
                continue

            parsed.update(included)

        # Parse defined variables
        elif line.startswith('#define'):
            k, v = line.split()[1:3]
            defined[k] = v

        if line.startswith('#'):
            continue

        k, v = line.split()[:2]

        # Retrieve defined value
        if (v in defined):
            v = defined[v]

        parsed[k.strip(string.punctuation)] = v

    return parsed
