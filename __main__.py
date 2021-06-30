"""
__main__.py

Script entrypoint
"""

from sys import argv
from typing import Tuple
from PyPDF4 import PdfFileMerger, PdfFileReader, PdfFileWriter


def split(file: PdfFileReader) -> Tuple([PdfFileWriter, PdfFileWriter]):
    count : int = file.getNumPages()
    pivot : int =  
    

print(argv)

p = PdfFileReader(argv[1])

print(p.getNumPages())