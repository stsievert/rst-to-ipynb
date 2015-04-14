
# rst-to-ipynb
This project converts between a standalone RESructured Text file and a IPython
notebook file.

## Example
`python convert.py tests/test.rst tests/test.ipynb` produces [test.ipynb] from
[test.rst].

[test.rst]:https://github.com/scottsievert/rst-to-ipynb/blob/master/tests/test.rst
[test.ipynb]:http://nbviewer.ipython.org/github/scottsievert/rst-to-ipynb/blob/master/tests/test.ipynb

## TODO:
* Properly parse args passing in; spaces/etc (anything with escape characters)
  are not supported
