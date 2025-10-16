# Log levels in practice

import logging
import sys

print("Log Levels in Practice")
print("-------------------\n")
for lvl in (
    logging.DEBUG, 
    logging.INFO, 
    logging.WARNING, 
    logging.ERROR, 
    logging.CRITICAL):
    print(f"Logging at level {logging.getLevelName(lvl):8} = {lvl}")
    print("---")
print("\n")

# Two-stage filtering

print("Two Stage Filtering in Practice")
print("--------------------------------\n")
filter_logger = logging.getLogger("demo.filter")
filter_logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.ERROR)
filter_logger.addHandler(stream_handler)


filter_logger.debug("INFO: will not be shown")
filter_logger.error("ERROR: will be shown")
print("\n")

# Configuring logs and handlers

print("Configuring logs and handlers in Practice")
print("------------------------------------------\n")

data_logger = logging.getLogger("demo.data")
data_logger.setLevel(logging.DEBUG)

data_sh = logging.StreamHandler(sys.stdout)
data_sh.setLevel(logging.ERROR)

data_fh = logging.FileHandler("process.log", "w")
data_fh.setLevel(logging.INFO)

data_logger.addHandler(data_sh)
data_logger.addHandler(data_fh)

data_logger.debug("DEBUG: will be shown in both console and file")
data_logger.info("INFO: will be shown in both console and file")
data_logger.warning("WARNING: will be shown in file but not in console")
data_logger.error("ERROR: will be shown in both console and file")
data_logger.critical("CRITICAL: will be shown in both console and file")