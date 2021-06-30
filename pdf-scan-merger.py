"""
__main__.py

Script entrypoint
"""

from sys import argv
from PyPDF4 import PdfFileReader, PdfFileWriter
from argparse import ArgumentParser, Namespace


# argparse
parser : ArgumentParser = ArgumentParser(
    description='Shuffle PDF pages, taking the first and last page each until reaching the middle of the document',
    allow_abbrev=True    
)
parser.add_argument(
    'path',
    type=str,
    help='path to source file'
)
parser.add_argument(
    '-o', '--out',
    type=str,
    help='path to output file (default: same as input file)'
)
args : Namespace = parser.parse_args()
# init vars
src : PdfFileReader = PdfFileReader(args.path)
out : PdfFileWriter = PdfFileWriter()
i : int = 0
j : int = src.getNumPages()-1
# main loop
while True:
    if j < i: break
    out.addPage(src.getPage(i))
    if j == i: break
    out.addPage(src.getPage(j))
    i += 1
    j -= 1
# output
p : str = args.out if args.out is not None else args.path
with open(p, 'wb') as f:
    out.write(f)
