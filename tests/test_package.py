from __future__ import annotations

import logging

import pytest

import fasthep_logging as m


def test_version() -> None:
    assert m.__version__


def test_getLogger() -> None:
    logger = m.get_logger("TESTLOGGER")
    assert logger.name == "TESTLOGGER"
    assert logger.level == m.DEFAULT_LOG_LEVEL
    assert logger.TRACE == m.TRACE  # type: ignore[attr-defined]
    assert logger.TIMING == m.TIMING  # type: ignore[attr-defined]


def test_trace(caplog: pytest.LogCaptureFixture) -> None:
    logger = m.get_logger("TESTLOGGER")
    caplog.set_level(logging.TRACE, logger="TESTLOGGER")  # type: ignore[attr-defined]
    logger.trace("test")  # type: ignore[attr-defined]
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.name == "TESTLOGGER"
    assert record.levelname == "TRACE"
    assert record.message == "test"


def test_timing(caplog: pytest.LogCaptureFixture) -> None:
    logger = m.get_logger("TESTLOGGER")
    caplog.set_level(logging.TIMING, logger="TESTLOGGER")  # type: ignore[attr-defined]
    logger.timing("test")  # type: ignore[attr-defined]
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.name == "TESTLOGGER"
    assert record.levelname == "TIMING"
    assert record.message == "test"
