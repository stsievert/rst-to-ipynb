from os import system
import argparse

"""
WHAT THIS FILE DOES:
    converts an RST file to a .ipynb file
HOW THIS FILE WORKS:
    1. calls pandoc to convert between .rst and .md
    2. calls notedown to convert between .md and .ipynb
TODO:
    * properly parse command line args (escape chars etc)
    * Features notedown needs:
        * figure emedding
        * unicode
DEPS:
    * [notedown], [pandoc]

[notedown]:https://github.com/aaren/notedown
[pandoc]:http://pandoc.org
"""

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("input_file", help="the input .rst file. Include the .rst")
parser.add_argument("output_file", help="the .ipynb output file. Include .ipynb")
args = parser.parse_args()

system('pandoc -i {0} -o tmp.md'.format(args.input_file))
system('notedown tmp.md -o {0}'.format(args.output_file))
system('rm tmp.md')
