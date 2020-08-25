#! /usr/bin/python3

import logging

logging.basicConfig(level = logging.DEBUG, format="%(asctime)s :: %(funcName)s :: %(lineno)d", filename='test.log')


logging.debug("this debug message")
logging.info("this info message")
logging.warning("this waringing message")
logging.error("this debug message")
logging.critical("this error message")
