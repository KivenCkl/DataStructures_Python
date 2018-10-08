import ctypes

class Array:
    """One-Demensional Arrays
    Parameters
    ----------
    size: int
        the size of array
    """

    def __init__(self, size):
        assert size > 0, 'array size must be > 0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'out of range'
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'out of range'
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
        
    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration


class Array2D:
    """Two-Demensional Arrays
    Parameters
    ----------
    numrows: int
        the size of rows
    numcols: int
        the size of cols
    Attributes
    ----------
    numRows()
    numCols()
    clear(value)
    getitem(i, j)
    setitem(i, j, val)
    """

    def __init__(self, numrows, numcols):
        self._the_rows = Array(numrows)
        for i in range(numrows):
            self._the_rows[i] = Array(numcols)
    
    @property
    def numRows(self):
        return len(self._the_rows)

    @property
    def numCols(self):
        return len(self._the_rows[0])

    def clear(self, value):
        for row in self._the_rows:
            row.clear(value)
    
    def __getitem__(self, ndx_tuple):
        """
        Parameters
        ----------
        ndx_tuple: tuple, shape = (row, col)
        Returns
        -------
        value
        """
        assert len(ndx_tuple) == 2
        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and
                col >= 0 and col < self.numCols)
        the_1d_array = self._the_rows[row]
        return the_1d_array[col]
    
    def __setitem__(self, ndx_tuple, value):
        """
        Parameters
        ----------
        ndx_tuple: tuple, shape = (row, col)
        value: int or float
        """
        assert len(ndx_tuple) == 2
        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and
                col >= 0 and col < self.numCols)
        the_1d_array = self._the_rows[row]
        the_1d_array[col] = value