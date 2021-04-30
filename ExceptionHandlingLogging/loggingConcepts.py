import logging

# Config logging
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

## Order of logging
logging.critical("Critical")
logging.error("Error")
logging.warning("warn")
logging.info("Info")
logging.debug("debug")
