from __future__ import annotations

import logging

from pytest import LogCaptureFixture

import fasthep_logging as m


def test_version():
    assert m.__version__


def test_getLogger():
    logger = m.get_logger("TESTLOGGER")
    assert logger.name == "TESTLOGGER"
    assert logger.level == m.DEFAULT_LOG_LEVEL
    assert logger.TRACE == m.TRACE
    assert logger.TIMING == m.TIMING


def test_trace(caplog: LogCaptureFixture):
    logger = m.get_logger("TESTLOGGER")
    caplog.set_level(logging.TRACE, logger="TESTLOGGER")
    logger.trace("test")
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.name == "TESTLOGGER"
    assert record.levelname == "TRACE"
    assert record.message == "test"


def test_timing(caplog: LogCaptureFixture):
    logger = m.get_logger("TESTLOGGER")
    caplog.set_level(logging.TIMING, logger="TESTLOGGER")
    logger.timing("test")
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.name == "TESTLOGGER"
    assert record.levelname == "TIMING"
    assert record.message == "test"
