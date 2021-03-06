Simple Python script to shuffle a PDF file such that it takes the first and last page of the current iteration and appends them to document, for instance ``1 2 3 4 5`` becomes ``1 5 2 4 3``. This would be useful when scanning a double-sided document.

### Usage

Either clone the repo and install PyPDF4 (``pip install pypdf4``), or download one of the executables from the releases page. Then run it like so:

```bash
$ python pdf-scan-merger.py .\path_to_source.pdf --out .\optional_path_to_output.pdf
```

```bash
$ pdf-scan-merger.exe .\path_to_source.pdf --out .\optional_path_to_output.pdf
```