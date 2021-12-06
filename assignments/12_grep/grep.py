#!/usr/bin/env python3
"""
Author : jcadogan <jcadogan@localhost>
Date   : 2021-12-05
Purpose: Rock the Casbah
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_files = len(args.files)

    for fh in args.files:
        for line in fh:
            if re.search(args.pattern, line,
                         re.IGNORECASE if args.insensitive else 0):
                print('{}{}'.format(f'{fh.name}:' if num_files > 1 else '',
                                    line),
                      end='',
                      file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
