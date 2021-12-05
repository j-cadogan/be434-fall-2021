#!/usr/bin/env python3
"""
Author : jcadogan <jcadogan@localhost>
Date   : 2021-12-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='Solfege',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    notes = args.positional
    solfege = {'Do': 'Do, A deer, a female deer',
               'Re': 'Re, A drop of golden sun',
               'Mi': 'Mi, A name I call myself',
               'Fa': 'Fa, A long long way to run',
               'Sol': 'Sol, A needle pulling thread',
               'La': 'La, A note to follow sol',
               'Ti': 'Ti, A drink with jam and bread'}

    for note in notes:
        if note in solfege.keys():
            print(solfege.get(note))
        else:
            print(f'I don\'t know "{note}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
