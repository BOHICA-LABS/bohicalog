"""
test json related things
"""
import json
import tempfile
from contextlib import redirect_stderr

import pytest

import bohicalog


def _test_json_obj_content(obj):
    # Check that all fields are contained
    attrs = [
        "asctime",
        "filename",
        "funcName",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "message",
        "name",
        "pathname",
        "process",
        "processName",
        "threadName",
    ]
    assert obj["message"] == "info"
    for attr in attrs:
        if attr not in obj:
            raise Exception("obj missing key '%s'" % attr)


@pytest.mark.skipif(reason="Fails when not ran on its own, need to investigate")
def test_json(capsys):
    """
    Test json logging
    """
    # Test setup_logger
    logger = bohicalog.setup_logger(json=True)
    logger.info("info")

    out, err = capsys.readouterr()

    _test_json_obj_content(json.loads(err))


def test_json_default_logger(capsys):
    """
    Test default logger
    :param capsys:
    :return:
    """
    # Test default logger
    bohicalog.reset_default_logger()
    bohicalog.logger.info("info")
    out, err = capsys.readouterr()
    assert "] info" in err

    bohicalog.json()
    bohicalog.logger.info("info")
    out, err = capsys.readouterr()
    _test_json_obj_content(json.loads(err))

    bohicalog.json(False)
    bohicalog.logger.info("info")
    out, err = capsys.readouterr()
    assert "] info" in err


def test_json_logfile(capsys):
    """
    Test json logging
    :param capsys:
    :return:
    """
    # Test default logger
    bohicalog.reset_default_logger()
    temp = tempfile.NamedTemporaryFile()
    try:
        logger = bohicalog.setup_logger(logfile=temp.name, json=True)
        logger.info("info")

        with open(temp.name) as f:
            content = f.read()
            _test_json_obj_content(json.loads(content))

    finally:
        temp.close()


def test_json_encoding(capsys):
    """
    see bohicalog.json(json_ensure_ascii=True)
    """
    bohicalog.reset_default_logger()

    # UTF-8 mode
    bohicalog.json(json_ensure_ascii=False)
    bohicalog.logger.info("??")
    out, err = capsys.readouterr()
    json.loads(err)  # make sure JSON is valid
    assert "??" in err
    assert "u00df" not in err

    # ASCII mode
    bohicalog.json(json_ensure_ascii=True)
    bohicalog.logger.info("??")
    out, err = capsys.readouterr()
    json.loads(err)  # make sure JSON is valid
    assert "u00df" in err
    assert "??" not in err

    # Default JSON mode should be utf-8
    bohicalog.json()
    bohicalog.logger.info("??")
    out, err = capsys.readouterr()
    json.loads(err)  # make sure JSON is valid
    assert "??" in err
    assert "u00df" not in err
