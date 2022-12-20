"""
This module contains the buffer class.
"""

from threading import RLock


class Buffer:
    """
    Buffer class for the telegram handler

    Usage:

    .. code-block:: python

        from bohicalog.handlers.telegram.buffer import Buffer

        buffer = Buffer(max_size=1000)
    """

    def __init__(self, max_size=None):
        """
        :param max_size: max size of the buffer
        """
        self._lock = RLock()
        self._buffer = ""
        self._max_size = max_size

    def write(self, data):
        """
        Write data to the buffer

        :param data: data to write
        """
        with self._lock:
            self._buffer = f"{self._buffer}\n{data}"[: self._max_size]

    def read(self, count):
        """
        Read data from the buffer

        :param count: count of data to read
        :rtype: str
        :return: data read
        """
        result = ""
        with self._lock:
            result, self._buffer = self._buffer[:count], self._buffer[count:]
        return result
