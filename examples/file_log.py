from fasthep_logging import TIMING, TRACE
from fasthep_logging import get_logger as flogger
from fasthep_logging._logging import FASTHEPLogger

logger = flogger("console_log", TIMING, "/tmp/console_log")

logger.info("This is an info message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
logger.timing("This is a timing message")
logger.trace("This is a trace message")

# example with codetiming

from codetiming import Timer
from time import sleep
with Timer(
    text="Elapsed time: {:.2f} seconds for sleeping 2 seconds",
    logger=logger.timing,
):
    sleep(2)
