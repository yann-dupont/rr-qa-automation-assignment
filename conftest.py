import logging
import pytest
import os
import sys

os.environ['PYPPETEER_CHROMIUM_REVISION'] = '1263111'

from requests_html import HTMLSession


@pytest.fixture(scope="session")
def session():
    return HTMLSession()

@pytest.fixture(scope="session")
def base_url():
    return 'https://tmdb-discover.surge.sh'

def pytest_configure(config):
    setup_logging()

def setup_logging():
    # Setting up logging
    logger = logging.getLogger()

    # Handler to write logs to a file
    file_handler = logging.FileHandler("test.log", mode='w')
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Handler to write logs to console
    console_handler = logging.StreamHandler(sys.__stdout__)
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.INFO)
    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)

class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, level):
       self.logger = logger
       self.level = level
       self.linebuf = ''

    def write(self, buf):
       for line in buf.rstrip().splitlines():
          self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass

    def isatty(self):
        return False
