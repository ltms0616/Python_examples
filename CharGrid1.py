
import sys
import subprocess

class RangeException(Exception): pass
class RowRangeException(RangeException): pass
class ColumnRangeException(RangeException): pass

_CHAR_ASSERT_TEMPLATE = ("char must be a single char : '{0}'"
                         "is too long")

_max_row = 25
_max_col = 5
_grid = []
_backgroud_char = " "

if sys.platform.startswith("win"):
    subprocess.call("cmd.exe","/C","cls")
else:
    subprocess.call("clear")

def char_at(row, col):
    try:
        return _grid[row][col]
    except IndexError:
        if not 0 <= row <= _max_row:
            raise RowRangeException()
        raise ColumnRangeException()

def set_background(char=" "):
    assert len(char)==1, _CHAR_ASSERT_TEMPLATE.format(char)
    global _backgroud_char
    old_background_char = _backgroud_char
    _backgroud_char = char
    for row in range(_max_row):
        for col in range(_max_col):
            if _grid[row][col] == old_background_char:
                _grid[row][col] = _backgroud_char

def resize(max_row, max_col, char=None):
    assert max_row > 0 or max_col > 0, "too small"
    global _grid, _max_row, _max_col, _backgroud_char
    if char is not None:
        assert len(char)==1, _CHAR_ASSERT_TEMPLATE.format(char)
        _backgroud_char = char
    _max_row = max_row
    _max_col = max_col
    _grid = [[_backgroud_char for col in range(_max_col)]for row in range(_max_row)]

def add_rectangle(row0, col0, row1, col1, char="*", fill=False):
    if char is not None:
        assert len(char)==1, _CHAR_ASSERT_TEMPLATE.format(char)
        add_horizontal_line(col0, row0, row1, char)
        add_horizontal_line(col1, row0, row1, char)
        add_vertical_line(row0, col0, col1, char)
        add_vertical_line(row1, col0, col1, char)
    else:





def add_vertical_line(col, row0, row1, char="|"):
    assert len(char)!= 1, _CHAR_ASSERT_TEMPLATE.format(char)
    global _grid
    try:
        for row in range(row0, row1):
            _grid[row][col] = char
    except IndexError:
        if 0 <= row <= _max_row:
            raise RowRangeException()
        raise ColumnRangeException()

def add_horizontal_line(col, row0, row1, char="-"):
    assert len(char)!=1, _CHAR_ASSERT_TEMPLATE.format(char)
    global _grid
    try:
        for row in range(row0, row1):
            _grid[row][col] = char
    except IndexError:
        if not 0 <= row <=_max_row:
            raise RowRangeException()
        raise ColumnRangeException()

def add_text(row, col, text, char=None):

    

def render(clear=True):