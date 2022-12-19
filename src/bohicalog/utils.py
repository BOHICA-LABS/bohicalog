"""
Module Level Utility Functions
"""


def check_key(dic, *keys):
    """
    Check if key exists in dictionary

    :param dic: dictionary to check
    :param key: key to check
    :return:
    """
    for key in keys:
        if key in dic.keys():
            return True
    return False
