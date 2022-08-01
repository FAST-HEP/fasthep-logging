from __future__ import annotations

import logging

from pytest import LogCaptureFixture

import fasthep_logging as m


def test_version():
    assert m.__version__


def test_getLogger():
    logger = m.getLogger("TESTLOGGER")
    assert logger.name == "TESTLOGGER"
    assert logger.level == m.DEFAULT_LOG_LEVEL
    assert logger.TRACE == m.TRACE
    assert logger.TIMING == m.TIMING


def test_trace(caplog: LogCaptureFixture):
    logger = m.getLogger("TESTLOGGER")
    caplog.set_level(logging.TRACE, logger="TESTLOGGER")
    logger.trace("test")
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.name == "TESTLOGGER"
    assert record.levelname == "TRACE"
    assert record.message == "test"
