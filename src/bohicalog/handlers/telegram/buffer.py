from threading import RLock

"""
This module contains the buffer class.
"""


class Buffer:
    """
    Buffer class for the telegram handler
    """

    def __init__(self, max_size=None):
        """
        Initialize the buffer
        :param max_size: max size of the buffer
        :param max_size:
        """
        self._lock = RLock()
        self._buffer = ""
        self._max_size = max_size

    def write(self, data):
        """
        Write data to the buffer
        :param data:
        :return:
        """
        with self._lock:
            self._buffer = f"{self._buffer}\n{data}"[: self._max_size]

    def read(self, count):
        """
        Read data from the buffer
        :param count:
        :return:
        """
        result = ""
        with self._lock:
            result, self._buffer = self._buffer[:count], self._buffer[count:]
        return result
